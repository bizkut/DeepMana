"""Effect for Deathwing, Mad Aspect (DRG_026).

Card Text: <b>Battlecry:</b> Attack ALL
other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass