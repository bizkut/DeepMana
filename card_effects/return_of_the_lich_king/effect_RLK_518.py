"""Effect for Silvermoon Sentinel (RLK_518).

Card Text: <b>Taunt</b>
<b>Manathirst (8):</b> Gain +2/+2 and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 8
        target._max_health += 8