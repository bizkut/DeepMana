# 📊 Simulator Analysis

> **Objective:** Ensure the simulator accurately reflects Hearthstone mechanics for valid RL training.

---

## 🧪 Verification Methodology

We employ a 3-layer verification strategy:

### 1. Unit Tests (`tests/`)
- **Mechanics**: Test basic rules (Taunt blocks attacks, Divine Shield absorbs damage).
- **Edge Cases**: Test interactions like Deathrattle ordering, full board summoning, hand size limits.

### 2. Auto-Validation Tool (`tools/verify_effects.py`)
- **LLM-Based Checking**: We loop through all 1800+ implemented card scripts.
- **Syntax Check**: Verify that `def setup(game, source):` signature is correct.
- **Logic Heuristics**: Check if a "Deal 3 damage" card actually calls `game.damage(..., 3)`.

### 3. Comparison with Ground Truth (Future)
- **Log Replay**: Take a real game log (`Power.log`) and replay the actions in our simulator.
- **Divergence Check**: If our state differs from the log state (e.g., different HP), we flag a bug.

---

## 🐛 Known Limitations (v1.0)

| Feature | Status | Notes |
|---------|--------|-------|
| **Graveyard Order** | ⚠️ | Exact timestamp order of death is simplified. |
| **Complex Triggers** | ⚠️ | "Whenever" vs "After" timing might be slightly off in nested chains. |
| **Magnetic** | ❌ | Not yet implemented. |
| **Tradeable** | ❌ | Not yet implemented. |
| **Locations** | ✅ | Fully supported. |
| **Titans** | 🚧 | Basic abilities work, but strict 1/turn limit needs testing. |

---

## 📈 Performance Metrics

- **Cloning Speed**: ~0.5ms per state clone.
- **Rollout Speed**: ~200 moves/sec on single core.
- **Memory Footprint**: ~50MB per specialized process.

---

## 🛠️ Debugging Tools

- **`game.print_board()`**: ASCII representation of the board state.
- **`game.history`**: Full list of actions taken in the game.
- **`Diff Tool`**: Compare two game states to find discrepancies.
