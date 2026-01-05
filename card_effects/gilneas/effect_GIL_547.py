"""Effect for Darius Crowley (GIL_547).

Card Text: [x]<b>Rush</b>
After this attacks and kills
a minion, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2