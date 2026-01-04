import os
import time
from typing import Callable, Optional

class LogWatcher:
    """
    Watches the Hearthstone Power.log for changes and triggers a callback for new lines.
    Handles the dynamic location of logs in recent Hearthstone versions.
    """
    
    POSSIBLE_ROOTS = [
        r"E:\JEU\Hearthstone\Logs",
        r"C:\Program Files (x86)\Hearthstone\Logs",
        r"D:\Jeux\Hearthstone\Logs",
        os.path.expandvars(r"%LocalAppData%\Blizzard\Hearthstone\Logs"),
    ]

    def __init__(self, callback: Callable[[str], None], skip_history: bool = False):
        self.callback = callback
        self.skip_history = skip_history
        self.log_path: Optional[str] = None
        self._running = False
        
    def find_power_log(self) -> Optional[str]:
        """Scans known locations for the most recent Power.log."""
        for root in self.POSSIBLE_ROOTS:
            if not os.path.exists(root):
                continue
                
            # Check for Power.log directly (Old definition)
            direct_path = os.path.join(root, "Power.log")
            if os.path.exists(direct_path):
                # check if it's recent? 
                pass
                
            # Check subdirectories (New definition, timestamped folders)
            subdirs = [os.path.join(root, d) for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
            if not subdirs:
                if os.path.exists(direct_path): return direct_path
                continue
                
            # Sort by modification time (newest first)
            subdirs.sort(key=lambda x: os.path.getmtime(x), reverse=True)
            
            # Look in newest folder
            for latest_dir in subdirs:
                log_path = os.path.join(latest_dir, "Power.log")
                if os.path.exists(log_path):
                    return log_path
        
        # Fallback check for direct path if no subdirs found valid
        return None

    def start(self):
        """Starts the watching loop (blocking)."""
        print("LogWatcher: Searching for Power.log...")
        self._running = True
        
        while not self.log_path and self._running:
            self.log_path = self.find_power_log()
            if not self.log_path:
                time.sleep(5)
                # We could callback status update here if we passed a status_callback
                
        if not self._running: return

        print(f"LogWatcher: Found {self.log_path}")
        self._running = True
        
        last_size = 0
        
        try:
            with open(self.log_path, "r", encoding="utf-8") as file:
                if self.skip_history:
                    # Skip to end - only read NEW lines
                    file.seek(0, 2)  # Seek to end
                    last_pos = file.tell()
                    print(f"LogWatcher: Skipping history, starting at position {last_pos}")
                else:
                    # Initial full read (for debugging/testing)
                    while True:
                        line = file.readline()
                        if not line: break
                        self.callback(line)
                    
                    last_pos = file.tell()
                    print(f"LogWatcher: Caught up to line {last_pos}")

            # Polling loop with reopen (handles file rotation/flush better)
            while self._running:
                try:
                    current_size = os.path.getsize(self.log_path)
                    if current_size > last_size:
                        with open(self.log_path, "r", encoding="utf-8") as file:
                            file.seek(last_pos)
                            while True:
                                line = file.readline()
                                if not line: break
                                self.callback(line)
                            last_pos = file.tell()
                            last_size = current_size
                    elif current_size < last_size:
                        # File truncated/rotated
                        last_pos = 0
                        last_size = 0
                    
                    time.sleep(0.5) # Poll every 500ms
                except OSError:
                    time.sleep(1) # Retry if locked
                    
        except Exception as e:
            print(f"LogWatcher Error: {e}")
            import traceback
            traceback.print_exc()
            
    def stop(self):
        self._running = False
