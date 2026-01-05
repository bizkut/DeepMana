"""
Inference Server for Multiprocessing Training.

Runs in main process and handles GPU inference requests from worker processes.
Workers send state tensors via queues, server returns policy/value predictions.
"""

import torch
import threading
import multiprocessing as mp
from multiprocessing import Queue
from typing import Optional, Tuple
import time
import queue


class InferenceServer:
    """
    Centralized GPU inference server for multiprocessing training.
    
    Workers send (worker_id, tensor_bytes) to request_queue.
    Server processes and sends (policy, value) to result_queues[worker_id].
    """
    
    def __init__(self, model: torch.nn.Module, num_workers: int, device: torch.device):
        self.model = model
        self.device = device
        self.num_workers = num_workers
        
        # Queues for IPC
        self.request_queue: Queue = mp.Queue()
        self.result_queues: dict = {i: mp.Queue() for i in range(num_workers)}
        
        # Control
        self._running = False
        self._thread: Optional[threading.Thread] = None
        
        # Stats
        self.total_requests = 0
        
    def start(self):
        """Start the inference server thread."""
        if self._running:
            return
            
        self._running = True
        self._thread = threading.Thread(target=self._serve_loop, daemon=True)
        self._thread.start()
        print(f"[InferenceServer] Started on {self.device}")
        
    def stop(self):
        """Stop the inference server."""
        self._running = False
        # Send poison pill to unblock queue
        self.request_queue.put(None)
        if self._thread:
            self._thread.join(timeout=2.0)
            self._thread = None
        print(f"[InferenceServer] Stopped. Total requests: {self.total_requests}")
        
    def _serve_loop(self):
        """Main loop: receive requests, run inference, send results."""
        self.model.to(self.device)
        self.model.eval()
        
        while self._running:
            try:
                request = self.request_queue.get(timeout=0.1)
                
                if request is None:  # Poison pill
                    break
                    
                worker_id, tensor_bytes, tensor_shape = request
                
                # Deserialize tensor
                tensor = torch.frombuffer(tensor_bytes, dtype=torch.float32).reshape(tensor_shape)
                tensor = tensor.to(self.device)
                
                # Run inference
                with torch.no_grad():
                    policy_logits, value = self.model(tensor)
                
                # Send result back
                policy_np = policy_logits.cpu().numpy().tobytes()
                value_float = value.item()
                
                self.result_queues[worker_id].put((policy_np, policy_logits.shape, value_float))
                self.total_requests += 1
                
            except queue.Empty:
                # Normal timeout, continue
                continue
            except Exception as e:
                print(f"[InferenceServer] ERROR: {e}")
                import traceback
                traceback.print_exc()
                continue
                
    def get_queues(self) -> Tuple[Queue, dict]:
        """Get queues for workers to use."""
        return self.request_queue, self.result_queues
