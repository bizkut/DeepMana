"""
Batch Neural Inference Server for MCTS.

Collects inference requests from multiple game workers and batches them
for efficient GPU utilization during training.
"""

import torch
import threading
import queue
import time
from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class InferenceRequest:
    """Container for an inference request."""
    tensor: torch.Tensor
    result_event: threading.Event
    policy: Optional[torch.Tensor] = None
    value: Optional[float] = None
    error: Optional[Exception] = None


class BatchInferenceServer:
    """
    Batches multiple MCTS inference requests for efficient GPU usage.
    
    Usage:
        server = BatchInferenceServer(model, max_batch_size=32)
        server.start()
        
        # From worker threads:
        policy, value = server.infer(state_tensor)
        
        # When done:
        server.stop()
    """
    
    def __init__(
        self,
        model: torch.nn.Module,
        max_batch_size: int = 32,
        timeout_ms: int = 10,
        device: Optional[torch.device] = None
    ):
        self.model = model
        self.max_batch_size = max_batch_size
        self.timeout_s = timeout_ms / 1000.0
        self.device = device or next(model.parameters()).device
        
        # Request queue
        self._queue: queue.Queue[InferenceRequest] = queue.Queue()
        
        # Control
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()
        
        # Metrics
        self.total_requests = 0
        self.total_batches = 0
        self.total_batch_size = 0
        
    def start(self):
        """Start the batch processing thread."""
        if self._running:
            return
            
        self._running = True
        self._thread = threading.Thread(target=self._batch_loop, daemon=True)
        self._thread.start()
        
    def stop(self):
        """Stop the batch processing thread."""
        self._running = False
        if self._thread:
            # Send poison pill to unblock queue
            self._queue.put(None)
            self._thread.join(timeout=2.0)
            self._thread = None
            
    def infer(self, tensor: torch.Tensor, timeout: float = 1.0) -> Tuple[torch.Tensor, float]:
        """
        Submit inference request and wait for result.
        
        Args:
            tensor: Input state tensor (1, input_dim)
            timeout: Max seconds to wait for result
            
        Returns:
            (policy_probs, value) tuple
            
        Raises:
            TimeoutError: If result not received in time
            RuntimeError: If inference failed
        """
        if not self._running:
            # Fallback to direct inference if server not running
            return self._direct_infer(tensor)
            
        request = InferenceRequest(
            tensor=tensor,
            result_event=threading.Event()
        )
        
        self._queue.put(request)
        
        # Wait for result
        if not request.result_event.wait(timeout=timeout):
            # Timeout - fallback to direct inference
            return self._direct_infer(tensor)
            
        if request.error:
            raise request.error
            
        return request.policy, request.value
        
    def _direct_infer(self, tensor: torch.Tensor) -> Tuple[torch.Tensor, float]:
        """Direct single-sample inference (fallback)."""
        self.model.eval()
        with torch.no_grad():
            tensor = tensor.to(self.device)
            if tensor.dim() == 1:
                tensor = tensor.unsqueeze(0)
            policy, value = self.model(tensor)
            return policy[0], value.item()
            
    def _batch_loop(self):
        """Main batch processing loop."""
        while self._running:
            batch = []
            deadline = time.time() + self.timeout_s
            
            # Collect requests until batch full or timeout
            while len(batch) < self.max_batch_size:
                remaining = deadline - time.time()
                if remaining <= 0:
                    break
                    
                try:
                    request = self._queue.get(timeout=remaining)
                    if request is None:  # Poison pill
                        break
                    batch.append(request)
                except queue.Empty:
                    break
                    
            if not batch:
                continue
                
            # Process batch
            self._process_batch(batch)
            
    def _process_batch(self, batch: list):
        """Process a batch of requests."""
        try:
            # Stack tensors
            tensors = []
            for req in batch:
                t = req.tensor
                if t.dim() == 1:
                    t = t.unsqueeze(0)
                tensors.append(t)
                
            batch_tensor = torch.cat(tensors, dim=0).to(self.device)
            
            # Batch inference
            self.model.eval()
            with torch.no_grad():
                policies, values = self.model(batch_tensor)
                
            # Distribute results
            for i, req in enumerate(batch):
                req.policy = policies[i]
                req.value = values[i].item()
                req.result_event.set()
                
            # Update metrics
            with self._lock:
                self.total_requests += len(batch)
                self.total_batches += 1
                self.total_batch_size += len(batch)
                
        except Exception as e:
            # Propagate error to all requests
            for req in batch:
                req.error = e
                req.result_event.set()
                
    @property
    def avg_batch_size(self) -> float:
        """Average batch size achieved."""
        if self.total_batches == 0:
            return 0.0
        return self.total_batch_size / self.total_batches
        
    def get_stats(self) -> dict:
        """Get inference statistics."""
        return {
            "total_requests": self.total_requests,
            "total_batches": self.total_batches,
            "avg_batch_size": self.avg_batch_size
        }
