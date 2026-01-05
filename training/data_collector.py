"""
Data Collector with Multiprocessing for DeepMana Training.

Uses separate worker processes for game simulation and a centralized
inference server for GPU model calls, bypassing Python's GIL.
"""

import sys
import os
import torch
import numpy as np
import time
from typing import List, Tuple, Optional, Dict
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp

# Path hacks (assuming run from root)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.model import HearthstoneModel
from ai.encoder import FeatureEncoder
from ai.replay_buffer import ReplayBuffer
from ai.inference_server import InferenceServer
from training.game_worker import play_game_process


class DataCollector:
    """
    Collects self-play games using multiprocessing.
    
    Uses InferenceServer in main process for GPU inference,
    worker processes for game simulation (bypassing GIL).
    """
    
    def __init__(self, model: HearthstoneModel, buffer: ReplayBuffer, num_workers: int = 4, device: torch.device = None):
        self.model = model
        self.buffer = buffer
        self.encoder = FeatureEncoder()
        self.num_workers = num_workers
        self.device = device or torch.device("cpu")
        self.stop_flag = False
        
        # Inference server (created on demand)
        self.inference_server: Optional[InferenceServer] = None
        
    def request_stop(self):
        """Request graceful stop of game collection."""
        self.stop_flag = True
        print("[DataCollector] Stop requested, finishing current games...")
        
    def shutdown(self):
        """Clean up resources."""
        self.stop_flag = True
        if self.inference_server:
            self.inference_server.stop()
            self.inference_server = None
            
    def _start_inference_server(self):
        """Start the inference server if not running."""
        if self.inference_server is None:
            self.inference_server = InferenceServer(
                self.model, 
                self.num_workers, 
                self.device
            )
            self.inference_server.start()
            
    def collect_games(self, num_games: int, mcts_sims: int = 25, verbose: bool = False) -> Dict[int, int]:
        """
        Collect self-play games using worker processes.
        
        Returns dict of {winner: count}.
        """
        # One-time buffer cleanup
        if len(self.buffer) > 0 and not hasattr(self, '_buffer_flushed'):
            print("Cleaning biased replay buffer...")
            self.buffer.clear()
            self._buffer_flushed = True
            
        print(f"Starting multiprocessing collection of {num_games} games with {self.num_workers} workers...")
        
        self.stop_flag = False
        start_time = time.time()
        winners = {0: 0, 1: 0, 2: 0}
        completed_games = 0
        
        # Start inference server
        self._start_inference_server()
        request_queue, result_queues = self.inference_server.get_queues()
        
        if self.num_workers == 0:
            # Sequential mode (for debugging)
            for i in range(num_games):
                if self.stop_flag:
                    break
                try:
                    trajectory, winner = play_game_process(
                        worker_id=0,
                        request_queue=request_queue,
                        result_queue=result_queues[0],
                        mcts_sims=mcts_sims,
                        verbose=verbose
                    )
                    self.buffer.add_game(trajectory, winner)
                    winners[winner] = winners.get(winner, 0) + 1
                    completed_games += 1
                    
                    elapsed = time.time() - start_time
                    avg_time = elapsed / completed_games
                    winner_str = f"Player {winner}" if winner > 0 else "Draw/Timeout"
                    print(f"[{completed_games}/{num_games}] Winner: {winner_str}. Buffer: {len(self.buffer)}. Avg: {avg_time:.2f}s/game")
                except Exception as e:
                    print(f"Sequential game failed: {e}")
        else:
            # Parallel mode with ProcessPoolExecutor
            # Note: We use spawn context to ensure clean process state
            ctx = mp.get_context('spawn')
            
            with ProcessPoolExecutor(max_workers=self.num_workers, mp_context=ctx) as executor:
                futures = []
                for i in range(num_games):
                    worker_id = i % self.num_workers  # Assign to worker slots
                    futures.append(executor.submit(
                        play_game_process,
                        worker_id=worker_id,
                        request_queue=request_queue,
                        result_queue=result_queues[worker_id],
                        mcts_sims=mcts_sims,
                        verbose=verbose
                    ))
                    
                # Collect results
                for future in as_completed(futures):
                    if self.stop_flag:
                        remaining = sum(1 for f in futures if not f.done())
                        print(f"[STOPPING] Cancelling {remaining} remaining games...")
                        for f in futures:
                            f.cancel()
                        break
                        
                    try:
                        trajectory, winner = future.result(timeout=120)
                        self.buffer.add_game(trajectory, winner)
                        winners[winner] = winners.get(winner, 0) + 1
                        completed_games += 1
                        
                        elapsed = time.time() - start_time
                        avg_time = elapsed / completed_games
                        winner_str = f"Player {winner}" if winner > 0 else "Draw/Timeout"
                        print(f"[{completed_games}/{num_games}] Winner: {winner_str}. Buffer: {len(self.buffer)}. Avg: {avg_time:.2f}s/game")
                    except Exception as e:
                        print(f"Worker process failed: {e}")
                        
        total_time = time.time() - start_time
        print(f"Collected {completed_games} games in {total_time:.1f}s ({total_time/max(completed_games,1):.2f}s/game)")
        return winners
