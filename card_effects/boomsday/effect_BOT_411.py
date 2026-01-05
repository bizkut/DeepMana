"""Effect for Electra Stormsurge (BOT_411).

Card Text: <b>Battlecry:</b> Your next spell this turn casts twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass