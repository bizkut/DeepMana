"""Effect for Whirling Stormdrake (TLC_243).

Card Text: <b>Rush</b>, <b>Windfury</b>
<b>Kindred:</b> Gain <b>Immune</b>
this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass