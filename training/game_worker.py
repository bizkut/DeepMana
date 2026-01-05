"""
Game Worker Process for Multiprocessing Training.

Each worker runs in a separate process, simulating games and requesting
neural network inference from the main process via queues.
"""

import os
import sys
import numpy as np
import torch
from multiprocessing import Queue
from typing import Tuple, List, Optional

# Ensure imports work
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai.encoder import FeatureEncoder
from ai.game_wrapper import HearthstoneGame
from ai.actions import Action, ACTION_SPACE_SIZE


class RemoteMCTS:
    """
    MCTS that uses remote inference via queues instead of local model.
    """
    
    def __init__(
        self, 
        worker_id: int,
        request_queue: Queue,
        result_queue: Queue,
        encoder: FeatureEncoder,
        c_puct: float = 1.0,
        num_simulations: int = 25
    ):
        self.worker_id = worker_id
        self.request_queue = request_queue
        self.result_queue = result_queue
        self.encoder = encoder
        self.c_puct = c_puct
        self.num_simulations = num_simulations
        self._temp_wrapper = HearthstoneGame()
        
        self._transposition_table = {}  # Cache: state_key -> (policy, value)
        self._max_cache_size = 10000
        
    def _get_state_key(self, wrapper_game) -> str:
        """Create cache key for game state."""
        g = wrapper_game.game
        p = wrapper_game.current_player
        # Key: turn + player + hand + board + mana + healths
        # This is a collision-prone simplification but fast
        return f"{g.turn}_{g.current_player_idx}_{len(p.hand)}_{len(p.board)}_{p.mana}_{p.hero.health if p.hero else 0}"

    def _remote_infer(self, state_tensor: torch.Tensor, wrapper_game=None) -> Tuple[torch.Tensor, float]:
        """Send tensor to inference server and wait for result."""
        # Check cache if wrapper is provided
        cache_key = None
        if wrapper_game:
            cache_key = self._get_state_key(wrapper_game)
            if cache_key in self._transposition_table:
                return self._transposition_table[cache_key]

        # Serialize tensor
        tensor_np = state_tensor.numpy()
        tensor_bytes = tensor_np.tobytes()
        tensor_shape = tensor_np.shape
        
        # Send request
        self.request_queue.put((self.worker_id, tensor_bytes, tensor_shape))
        
        # Wait for result (blocking)
        policy_bytes, policy_shape, value = self.result_queue.get()
        
        # Deserialize result
        policy = torch.from_numpy(
            np.frombuffer(policy_bytes, dtype=np.float32).copy().reshape(policy_shape)
        )
        
        # Update cache
        if cache_key:
            if len(self._transposition_table) > self._max_cache_size:
                self._transposition_table.clear()  # Simple eviction
            self._transposition_table[cache_key] = (policy, value)
            
        return policy, value
        
    def search(self, game_state, root_node=None) -> Tuple[List[float], object]:
        """
        Run MCTS with remote inference.
        Returns action probabilities.
        """
        from ai.mcts import MCTSNode  # Import here to avoid circular
        
        if root_node:
            root = root_node
            root.state = game_state
        else:
            root = MCTSNode(state=game_state, parent=None)
        
        # Add Dirichlet noise to root for exploration (AlphaZero style)
        if not root.is_expanded:
            self._expand_with_noise(root, is_root=True)
        else:
            self._add_noise_to_root(root)
        
        for _ in range(self.num_simulations):
            node = root
            
            # Selection - iterate over dict values
            while node.is_expanded and node.children:
                node = self._select_child(node)
                
            # Expansion & Evaluation
            if not node.is_terminal():
                value = self._expand(node)
            else:
                value = self._terminal_value(node)
                
            # Backpropagation  
            self._backprop(node, value)
            
        # Get action probabilities
        action_probs = self._get_action_probs(root)
        return action_probs, root
    
    def _add_noise_to_root(self, root):
        """Add Dirichlet noise to existing root children for exploration."""
        if not root.children:
            return
        epsilon = 0.40  # Weight of noise vs prior (increased from 0.25)
        alpha = 0.15  # Dirichlet concentration (lower = more varied, decreased from 0.3)
        
        noise = np.random.dirichlet([alpha] * len(root.children))
        for i, child in enumerate(root.children.values()):
            child.prior_prob = (1 - epsilon) * child.prior_prob + epsilon * noise[i]
    
    def _expand_with_noise(self, node, is_root=False) -> float:
        """Expand node and add Dirichlet noise if root."""
        value = self._expand(node)
        if is_root:
            self._add_noise_to_root(node)
        return value
        
    def _select_child(self, node):
        """UCB selection."""
        best_score = -float('inf')
        best_child = None
        
        for child in node.children.values():  # dict values
            if child.visit_count == 0:
                ucb = float('inf')
            else:
                q = child.value_sum / child.visit_count
                u = self.c_puct * child.prior_prob * np.sqrt(node.visit_count) / (1 + child.visit_count)
                ucb = q + u
                
            if ucb > best_score:
                best_score = ucb
                best_child = child
                
        return best_child
        
    def _expand(self, node) -> float:
        """Expand node using remote inference."""
        # Set up wrapper
        p_idx = 0 if node.state.current_player == node.state.players[0] else 1
        self._temp_wrapper.perspective = p_idx + 1
        self._temp_wrapper._game = node.state
        state_data = self._temp_wrapper.get_state()
        
        # Encode and send for inference
        tensor = self.encoder.encode(state_data).unsqueeze(0)
        policy_probs, value = self._remote_infer(tensor, wrapper_game=self._temp_wrapper)
        
        # Get valid actions
        valid_actions = self._temp_wrapper.get_valid_actions()
        node.is_expanded = True
        
        # Create children
        from ai.mcts import MCTSNode
        for act_obj in valid_actions:
            act_idx = act_obj.to_index()
            prior = policy_probs[0, act_idx].item() if act_idx < policy_probs.shape[1] else 0.01
            
            child_state = node.state.clone()
            self._temp_wrapper._game = child_state
            self._temp_wrapper.step(act_obj)
            
            child = MCTSNode(
                state=child_state, 
                parent=node, 
                action_idx=act_idx,
                action_obj=act_obj
            )
            child.prior_prob = max(prior, 0.01)
            node.children[act_idx] = child  # dict keyed by action index
            
        return value
        
    def _terminal_value(self, node) -> float:
        """Get value for terminal state."""
        if not node.state.ended:
            return 0.0
        winner = node.state.winner
        if winner is None:
            return 0.0
        p_idx = 0 if node.state.current_player == node.state.players[0] else 1
        return 1.0 if winner == node.state.players[p_idx] else -1.0
        
    def _backprop(self, node, value):
        """Backpropagate value."""
        while node:
            node.visit_count += 1
            node.value_sum += value
            value = -value  # Flip for opponent
            node = node.parent
            
    def _get_action_probs(self, root) -> List[float]:
        """Get action probabilities from visit counts."""
        probs = [0.0] * ACTION_SPACE_SIZE
        total_visits = sum(c.visit_count for c in root.children.values())
        
        if total_visits > 0:
            for child in root.children.values():
                idx = child.action_obj.to_index()
                probs[idx] = child.visit_count / total_visits
                
        return probs


def play_game_process(
    worker_id: int,
    request_queue: Queue,
    result_queue: Queue,
    mcts_sims: int,
    verbose: bool = False,
    force_play: bool = True  # New flag
) -> Tuple[List, int]:
    # ... (init code) ...
    # Initialize components
    from simulator import CardDatabase
    db = CardDatabase.get_instance()
    if not db.is_loaded: db.load()
    encoder = FeatureEncoder()
    perspective = 1 if np.random.random() > 0.5 else 2
    pid = os.getpid()
    if verbose: print(f"  [Worker {pid}] Starting Game (Perspective: P{perspective})")
    env = HearthstoneGame(perspective=perspective)
    env.reset()
    trajectory = []
    step_count = 0
    max_steps = 500
    
    mcts = RemoteMCTS(worker_id, request_queue, result_queue, encoder, num_simulations=mcts_sims)
    root_node = None
    
    from ai.actions import ActionType
    
    while not env.is_game_over and step_count < max_steps:
        # Update perspective
        current_p_idx = 0 if env.game.current_player == env.game.players[0] else 1
        env.perspective = current_p_idx + 1
        
        state = env.get_state()
        valid_actions = env.get_valid_actions()
        if not valid_actions: break
        
        # MCTS search
        action_probs, root_node = mcts.search(env.game, root_node)
        
        # Apply Force Play logic: Mask END_TURN if we have plays/attacks
        if force_play:
            has_plays = any(a.action_type in (ActionType.PLAY_CARD, ActionType.ATTACK, ActionType.HERO_POWER) for a in valid_actions)
            if has_plays:
                # Zero out END_TURN probability
                for i, act in enumerate(valid_actions):
                    if act.action_type == ActionType.END_TURN:
                        idx = act.to_index()
                        action_probs[idx] = 0.0
        
        # Sample action
        valid_indices = [a.to_index() for a in valid_actions]
        valid_probs = [action_probs[i] for i in valid_indices]
        prob_sum = sum(valid_probs)
        if prob_sum > 0:
            valid_probs = [p / prob_sum for p in valid_probs]
        else:
            # Fallback (e.g. if we masked END_TURN but it was the only prob)
            valid_probs = [1.0 / len(valid_actions)] * len(valid_actions)
            
        chosen_idx = np.random.choice(len(valid_actions), p=valid_probs)
        chosen_action = valid_actions[chosen_idx]
        
        # Store transition
        encoded = encoder.encode(state)
        trajectory.append((encoded.numpy(), action_probs, env.perspective))
        
        # Execute action
        env.step(chosen_action)
        step_count += 1
        
        if verbose and step_count % 20 == 0:
            print(f"  [Worker {pid}] Step {step_count}...")
            
    # Determine winner
    if env.game.winner:
        winner = 1 if env.game.winner == env.game.players[0] else 2
    else:
        winner = 0  # Draw/timeout
        
    if verbose:
        print(f"  [Worker {pid}] Game FINISHED at step {step_count}.")
        
    return trajectory, winner
