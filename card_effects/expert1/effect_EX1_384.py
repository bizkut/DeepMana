"""Effect for Avenging Wrath (EX1_384).

Card Text: Deal $8 damage randomly split among all enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 8, source)