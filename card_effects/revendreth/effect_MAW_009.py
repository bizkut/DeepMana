"""Effect for Shadehound (MAW_009).

Card Text: [x]Whenever this attacks, give
your other Beasts +2/+2.
<b>Infuse (3 Beasts):</b>
Gain <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2