# 🎮 Phase 0: Universal Simulator

> **Goal:** Build a robust, lightweight, and extensible Hearthstone engine in Python.

Unlike existing projects (Fireplace, Sabberstone), our simulator is designed specifically for **Reinforcement Learning**:
- **Speed**: Optimized for cloning and MCTS simulations.
- **LLM-Friendly**: Card effects are generated and verified by LLMs.
- **Flexibility**: Supports custom game modes and rapid prototyping.
- **Observability**: Full access to internal state vectors.

---

## 🏗️ Architecture

### 1. The Core (`simulator/`)

The core is built around a few main classes:

- **`Game`**: The central orchestrator. Manages the turn loop, event queue, and game zones.
- **`Player`**: Represents a player (hero, hand, deck, mana, secrets).
- **`Entity`**: Base class for everything (Cards, Heroes, Powers).
- **`Card`**: A specific instance of a card with dynamic stats (Attack/Health/Cost).

### 2. Event System

We use an **Event-Driven Architecture**:
1. An action (Play Card) is pushed to the queue.
2. The action triggers an event (`on_card_played`).
3. Registered listeners (Secrets, Trigger Minions) react to the event.
4. Reactions can push new events (Death, Summon) to the stack.

This allows for complex interactions like "After you cast a spell, cast it again" to be handled natively.

### 3. Card Loading (`card_loader.py`)

Cards are loaded from `hearthstone_data` JSON definitions.
- **Static Data**: Name, Cost, ID, Text.
- **Dynamic Scripts**: We use a `card_effects/` directory where Python scripts implement the logic for each card ID (e.g., `effect_CORE_EX1_012.py`).

---

## 🧩 Key Decisions

### Why simulate instead of using the Game Client?
- **Speed**: The game client is too slow for training (animations, network). Our simulator can run 1000s of games per second.
- **State Access**: We need the perfect information state for the Value Network, not just what is visible on screen.

### Handling "Randomness"
For consistent MCTS, we need deterministic simulations. We control the RNG seed to ensure that a simulation of a specific branch always yields the same result for the same random seed.

---

## 📈 Current Status

- **Basic Mechanics**: ✅ Minions, Spells, Weapons, Hero Powers.
- **Keywords**: ✅ Taunt, Divine Shield, Rush, Charge, Windfury, Reborn.
- **Advanced**: ✅ Discover (partially), Secret (scaffolding).
- **Card Pool**: 1800+ cards validated.

---

## 📚 References
- [Hearthstone Data Repository](https://github.com/HearthSim/hearthstone-data)
- [Fireplace Engine (Legacy)](https://github.com/jleclanche/fireplace)
