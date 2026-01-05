"""Effect for Kil'jaeden (GDB_145).

Card Text: [x]<b>Battlecry:</b> Replace your deck with an endless portal of Demons. Each turn, they gain an additional +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
