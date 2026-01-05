"""Effect for Unwilling Sacrifice (ICC_469).

Card Text: Choose a friendly minion. Destroy it and a random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()