"""
AIBrain - Interface between AlphaZero model and the overlay.

This module provides a high-level interface to use the trained model
for suggesting actions during live gameplay.
"""

import os
import torch
import numpy as np
from typing import Optional, Tuple, List

from ai.model import HearthstoneModel
from ai.encoder import FeatureEncoder
from ai.actions import Action, ActionType
from ai.game_wrapper import HearthstoneGame
from ai.game_state import GameState


class AIBrain:
    """
    High-level AI interface for the overlay.
    
    Usage:
        brain = AIBrain()
        brain.load_model("models/checkpoint_iter_100.pt")
        action, confidence = brain.suggest_action(game_state)
    """
    
    def __init__(self, input_dim: int = 870, action_dim: int = 300, use_gpu: bool = True):
        self.input_dim = input_dim
        self.action_dim = action_dim
        
        # Device selection using centralized utility (respects config settings)
        if use_gpu:
            from ai.device import get_compute_device
            self.device = get_compute_device()
        else:
            self.device = torch.device("cpu")
        
        # Initialize model
        self.model = HearthstoneModel(input_dim, action_dim).to(self.device)
        self.encoder = FeatureEncoder()
        
        # State
        self.model_loaded = False
        self.model_path = None
        
    def load_model(self, path: str) -> bool:
        """Load a trained model checkpoint."""
        if not os.path.exists(path):
            print(f"Model not found: {path}")
            return False
            
        try:
            checkpoint = torch.load(path, map_location=self.device)
            # Handle both full checkpoint (dict) and direct state_dict
            if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
                self.model.load_state_dict(checkpoint['model_state_dict'])
            else:
                self.model.load_state_dict(checkpoint)
            self.model.eval()
            self.model_loaded = True
            self.model_path = path
            print(f"Model loaded from {path}")
            return True
        except Exception as e:
            print(f"Failed to load model: {e}")
            return False
    
    def load_latest_model(self, models_dir: str = "models") -> bool:
        """Load the most recent checkpoint from models directory."""
        if not os.path.exists(models_dir):
            print(f"Models directory not found: {models_dir}")
            return False
        
        # Prefer latest_model.pt (shared via GitHub)
        latest_model_path = os.path.join(models_dir, "latest_model.pt")
        if os.path.exists(latest_model_path):
            return self.load_model(latest_model_path)
            
        # Fall back to highest-numbered checkpoint
        checkpoints = [f for f in os.listdir(models_dir) if f.startswith('checkpoint_iter_') and f.endswith('.pt')]
        if not checkpoints:
            print("No checkpoints found")
            return False
            
        # Sort by iteration number (assumes format: checkpoint_iter_X.pt)
        def get_iter(name):
            try:
                return int(name.split('_')[-1].replace('.pt', ''))
            except:
                return 0
                
        checkpoints.sort(key=get_iter, reverse=True)
        latest = os.path.join(models_dir, checkpoints[0])
        
        return self.load_model(latest)
    
    def suggest_action(self, state: GameState) -> Tuple[Optional[Action], float, str]:
        """
        Get the best action for the current game state.
        
        Args:
            state: GameState object from the simulator/parser
            
        Returns:
            (action, confidence, description)
        """
        if not self.model_loaded:
            return None, 0.0, "Model not loaded"
            
        try:
            # Encode state to tensor
            state_tensor = self.encoder.encode(state).unsqueeze(0).to(self.device)
            
            # Get model prediction
            self.model.eval()
            with torch.no_grad():
                policy, value = self.model(state_tensor)
            
            # Policy is action probabilities
            probs = policy.cpu().numpy()[0]
            
            # Get valid actions mask from state directly (more reliable)
            valid_mask = self._get_valid_action_mask_from_state(state)
            
            # Debug Logic
            print(f"[Brain] Mana: {state.friendly_player.mana}/{state.friendly_player.max_mana}")
            print(f"[Brain] Hand: {[(c.info.name if c else 'None', c.current_cost if c else -1) for c in state.friendly_player.hand]}")
            
            masked_probs = probs * valid_mask
            
            # Normalize
            if masked_probs.sum() > 0:
                masked_probs = masked_probs / masked_probs.sum()
            else:
                print(f"[Brain] WARN: All actions masked! Mask sum: {valid_mask.sum()}")
                # Fallback: End Turn
                return Action.end_turn(), 1.0, "End Turn (forced)"
            
            # Get best action
            best_idx = np.argmax(masked_probs)
            confidence = float(masked_probs[best_idx])
            
            # Debug: what did the model want vs what did it get?
            raw_best = np.argmax(probs)
            if raw_best != best_idx:
                print(f"[Brain] Model wanted {raw_best} ({probs[raw_best]:.2f}) but mask forced {best_idx}")
            
            action = Action.from_index(best_idx)
            description = self._action_to_description(action, state)
            
            return action, confidence, description
            
        except Exception as e:
            print(f"Error in suggest_action: {e}")
            import traceback
            traceback.print_exc()
            return None, 0.0, f"Error: {e}"

    def _get_valid_action_mask_from_state(self, state: GameState) -> np.ndarray:
        """Create mask from GameState object."""
        mask = np.zeros(self.action_dim, dtype=np.float32)
        
        p = state.friendly_player
        
        # 0. End Turn (Action 0)
        mask[0] = 1.0
        
        # 1. Hero Power (Action 1 for simple usage)
        if p.hero_power:
            hp_cost = p.hero_power.cost
            hp_usable = p.hero_power.is_usable
            if hp_usable and (hp_cost <= p.mana):
                mask[1] = 1.0
            # Debug
            if hp_usable:
                print(f"[Brain] Hero Power: cost={hp_cost}, mana={p.mana}, allowed={hp_cost <= p.mana}")

        # 2. Play Card (Indices 11, 31, 51... for simple play)
        # Structure from actions.py: 11 + (card_index * 20) = Play Card (no target)
        playable_actions = []
        for i, card in enumerate(p.hand):
            if i >= 10: break # Action space limited to 10 cards
            
            # Have enough mana?
            if card.current_cost <= p.mana:
                # Calculate correct action index for simple play
                # Base offset for play actions is 11
                # Each card has 20 slots (1 simple + target variations)
                action_idx = 11 + (i * 20)
                if action_idx < self.action_dim:
                    mask[action_idx] = 1.0
                    playable_actions.append(f"Card {i} ({card.info.name if card.info else 'Unknown'})")
        
        if playable_actions:
            print(f"[Brain] Playable card actions: {playable_actions}")
            
        # 3. Attack (Indices 211+)
        # Simplified: allow simple attacks if we impl logic later
        # For now, just focusing on fixing the critical Play Card / End Turn bug
        
        return mask
    
    def get_value_estimate(self, state: GameState) -> float:
        """Get the model's value estimate for the current state (-1 to 1)."""
        if not self.model_loaded:
            return 0.0
            
        try:
            state_tensor = self.encoder.encode(state).unsqueeze(0).to(self.device)
            self.model.eval()
            with torch.no_grad():
                _, value = self.model(state_tensor)
                
            return float(value.cpu().numpy()[0])
        except:
            return 0.0
    
    def _action_to_description(self, action: Action, state: GameState) -> str:
        """Convert action to human-readable description."""
        if action.action_type == ActionType.END_TURN:
            return "End Turn"
            
        elif action.action_type == ActionType.PLAY_CARD:
            p = state.friendly_player
            if action.card_index is not None and action.card_index < len(p.hand):
                card = p.hand[action.card_index]
                card_name = getattr(card, 'name', f'Card {action.card_index}')
                return f"Play: {card_name}"
            return f"Play card {action.card_index}"
            
        elif action.action_type == ActionType.HERO_POWER:
            return "Use Hero Power"
            
        elif action.action_type == ActionType.ATTACK:
            return f"Attack: Minion {action.attacker_index} → Target {action.target_index}"
            
        elif action.action_type == ActionType.USE_LOCATION:
            return f"Activate Location {action.card_index}"
            
        return str(action)


# Singleton instance for easy access
_brain_instance: Optional[AIBrain] = None

def get_brain() -> AIBrain:
    """Get the global AIBrain instance."""
    global _brain_instance
    if _brain_instance is None:
        _brain_instance = AIBrain()
    return _brain_instance
