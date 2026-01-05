"""Effect for Aldor Peacekeeper (EX1_382).

Card Text: <b>Battlecry:</b> Change an enemy minion's Attack to 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass