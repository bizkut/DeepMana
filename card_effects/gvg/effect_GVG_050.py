"""Effect for Bouncing Blade (GVG_050).

Card Text: Deal $1 damage to a random minion. Repeat until a minion dies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)