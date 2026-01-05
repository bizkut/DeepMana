"""
IPC Bridge for macOS Native Overlay.
Broadcasts overlay data via Unix domain socket for Swift client consumption.
"""

import json
import os
import platform
import socket
import threading
import queue
from dataclasses import dataclass, asdict
from typing import Optional, Tuple, List

SOCKET_PATH = "/tmp/deepmana_overlay.sock"


@dataclass
class OverlayMessage:
    """Message structure for overlay IPC."""
    type: str  # "arrow", "highlight", "actions", "status", "winrate", "mana"
    data: dict


class OverlayBridge:
    """
    Broadcasts overlay state to native macOS app via Unix socket.
    Thread-safe, non-blocking design.
    Sends coordinates as percentages (0.0–1.0) for resolution independence.
    """
    
    def __init__(self, geometry_width: int = 1920, geometry_height: int = 1080):
        self.running = False
        self.socket_path = SOCKET_PATH
        self.server_socket: Optional[socket.socket] = None
        self.clients: List[socket.socket] = []
        self.message_queue: queue.Queue = queue.Queue()
        self._server_thread: Optional[threading.Thread] = None
        self._broadcast_thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()
        # Store geometry dimensions for converting to percentages
        self.geometry_width = geometry_width
        self.geometry_height = geometry_height
        
    def start(self):
        """Start the IPC server."""
        if self.running:
            return
            
        # Clean up old socket
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)
            
        self.running = True
        
        # Create Unix domain socket
        self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(self.socket_path)
        self.server_socket.listen(5)
        self.server_socket.settimeout(1.0)  # For graceful shutdown
        
        # Start threads
        self._server_thread = threading.Thread(target=self._accept_clients, daemon=True)
        self._server_thread.start()
        
        self._broadcast_thread = threading.Thread(target=self._broadcast_loop, daemon=True)
        self._broadcast_thread.start()
        
        print(f"[OverlayBridge] IPC server started at {self.socket_path}")
        
    def stop(self):
        """Stop the IPC server."""
        self.running = False
        
        # Close all clients
        with self._lock:
            for client in self.clients:
                try:
                    client.close()
                except:
                    pass
            self.clients.clear()
        
        # Close server
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
            self.server_socket = None
            
        # Clean up socket file
        if os.path.exists(self.socket_path):
            try:
                os.unlink(self.socket_path)
            except:
                pass
                
        print("[OverlayBridge] IPC server stopped")
        
    def _accept_clients(self):
        """Accept incoming client connections."""
        while self.running:
            try:
                client, _ = self.server_socket.accept()
                with self._lock:
                    self.clients.append(client)
                print(f"[OverlayBridge] Client connected ({len(self.clients)} total)")
            except socket.timeout:
                continue
            except Exception as e:
                if self.running:
                    print(f"[OverlayBridge] Accept error: {e}")
                break
                
    def _broadcast_loop(self):
        """Broadcast messages to all connected clients."""
        while self.running:
            try:
                # Block for up to 100ms waiting for messages
                try:
                    msg = self.message_queue.get(timeout=0.1)
                except queue.Empty:
                    continue
                    
                # Serialize message
                json_data = json.dumps(msg) + "\n"
                data = json_data.encode('utf-8')
                
                # Send to all clients
                dead_clients = []
                with self._lock:
                    for client in self.clients:
                        try:
                            client.sendall(data)
                        except (BrokenPipeError, ConnectionResetError, OSError):
                            dead_clients.append(client)
                            
                    # Remove dead clients
                    for client in dead_clients:
                        self.clients.remove(client)
                        try:
                            client.close()
                        except:
                            pass
                        
                if dead_clients:
                    print(f"[OverlayBridge] Removed {len(dead_clients)} disconnected client(s)")
                    
            except Exception as e:
                if self.running:
                    print(f"[OverlayBridge] Broadcast error: {e}")
                    
    def _send(self, msg_type: str, data: dict):
        """Queue a message for broadcast."""
        self.message_queue.put({"type": msg_type, "data": data})
        
    # === Public API (matches OverlayWindow interface) ===
    
    def set_geometry_size(self, width: int, height: int):
        """Update the geometry dimensions (called when window size changes)."""
        self.geometry_width = width
        self.geometry_height = height
        
    def set_arrow(self, start, end):
        """Send arrow coordinates as percentages (0.0–1.0)."""
        if start and end:
            self._send("arrow", {
                "start": {"x": start.x / self.geometry_width, "y": start.y / self.geometry_height},
                "end": {"x": end.x / self.geometry_width, "y": end.y / self.geometry_height}
            })
        else:
            self._send("arrow", {"start": None, "end": None})
            
    def set_highlight(self, pos):
        """Send highlight position as percentage (0.0–1.0)."""
        if pos:
            self._send("highlight", {
                "x": pos.x / self.geometry_width, 
                "y": pos.y / self.geometry_height
            })
        else:
            self._send("highlight", None)
            
    def set_action_queue(self, actions: list):
        """Send action queue."""
        # actions is list of (type, desc, details) tuples
        action_list = [
            {"type": a[0], "desc": a[1], "details": a[2]} 
            for a in actions
        ]
        self._send("actions", {"items": action_list})
        
    def update_status(self, text: str):
        """Send status text."""
        self._send("status", {"text": text})
        
    def update_info(self, text: str):
        """Send info text."""
        self._send("info", {"text": text})
        
    def update_winrate(self, value: float):
        """Send winrate (value is -1 to 1, convert to 0-100%)."""
        pct = int(((value + 1) / 2) * 100)
        self._send("winrate", {"percent": pct})
        
    def update_mana(self, current: int, maximum: int):
        """Send mana values."""
        self._send("mana", {"current": current, "max": maximum})
        
    def show(self):
        """Start and show (for compatibility with OverlayWindow)."""
        self.start()
        
    def close(self):
        """Stop (for compatibility with OverlayWindow)."""
        # Attempt to tell client to quit gracefully
        try:
            self._send("quit", {})
            # Give it a moment to flush
            import time
            time.sleep(0.1)
        except:
            pass
        self.stop()


def is_macos() -> bool:
    """Check if running on macOS."""
    return platform.system() == "Darwin"


def get_overlay():
    """
    Factory function to get the appropriate overlay.
    Returns OverlayBridge on macOS, None on Windows (caller should use PyQt6).
    """
    if is_macos():
        bridge = OverlayBridge()
        return bridge
    return None
