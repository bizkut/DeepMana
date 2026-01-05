"""Effect for Marshland Thresher (TLC_256).

Card Text: After you cast a spell,
gain <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass