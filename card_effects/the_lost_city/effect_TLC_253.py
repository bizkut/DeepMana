"""Effect for Petrified Ogre (TLC_253).

Card Text: [x]Starts <b>Dormant. </b>While
<b>Dormant</b>, gain +2/+2 at the
start of your turn. <i>(50% chance
to awaken instead.)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2