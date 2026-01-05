"""Effect for Pressure Plate (ULD_152).

Card Text: <b>Secret:</b> After your opponent casts a spell, destroy a random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()