"""Effect for Tour Guide (SCH_312).

Card Text: <b>Battlecry:</b> Your next Hero Power costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass