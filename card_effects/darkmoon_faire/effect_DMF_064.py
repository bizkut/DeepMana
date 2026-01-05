"""Effect for Carousel Gryphon (DMF_064).

Card Text: <b>Divine Shield</b>
<b>Corrupt:</b> Gain +3/+3 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3