"""Effect for Lightning Rod (TIME_212).

Card Text: Deal $2 damage to a friendly minion to deal $4 damage to a random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)