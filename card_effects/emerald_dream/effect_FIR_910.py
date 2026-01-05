"""Effect for Scorching Winds (FIR_910).

Card Text: Deal $3 damage. Discard a random Fire spell to deal $3 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)