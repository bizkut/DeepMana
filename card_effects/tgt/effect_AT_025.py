"""Effect for Dark Bargain (AT_025).

Card Text: Destroy 2 random enemy minions. Discard 2 random cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()