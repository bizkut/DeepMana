"""Effect for Arcane Barrage (TIME_855).

Card Text: Deal $3 damage to an enemy and $2 damage to two other random ones.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)