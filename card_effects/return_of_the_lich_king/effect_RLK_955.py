"""Effect for Silvermoon Armorer (RLK_955).

Card Text: [x]<b>Rush</b>
<b>Manathirst (7):</b> Gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 7
        target._max_health += 7