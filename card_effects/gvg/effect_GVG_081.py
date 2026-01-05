"""Effect for Gilblin Stalker (GVG_081).

Card Text: <b>Stealth</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass