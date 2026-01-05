"""Effect for Icehoof Protector (AV_133).

Card Text: <b>Taunt</b>
<b>Freeze</b> any character damaged by this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True