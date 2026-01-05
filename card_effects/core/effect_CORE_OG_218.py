"""Effect for Bloodhoof Brave (CORE_OG_218).

Card Text: <b>Taunt</b> Has +3 Attack while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
