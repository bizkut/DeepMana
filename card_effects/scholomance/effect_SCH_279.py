"""Effect for Trueaim Crescent (SCH_279).

Card Text: After your Hero attacks a minion, your minions attack it too.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass