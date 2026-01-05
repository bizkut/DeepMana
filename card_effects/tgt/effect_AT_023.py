"""Effect for Void Crusher (AT_023).

Card Text: <b>Inspire:</b> Destroy a random minion for each player.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()