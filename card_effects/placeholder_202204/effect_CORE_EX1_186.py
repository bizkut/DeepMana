"""Effect for SI:7 Infiltrator (CORE_EX1_186).

Card Text: <b>Battlecry:</b> Destroy a random enemy <b>Secret</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()