"""Effect for Steamwheedle Sniper (GVG_087).

Card Text: Your Hero Power can target minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass