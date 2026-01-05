"""Effect for Ghost Light Angler (GIL_678).

Card Text: <b>Echo</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass