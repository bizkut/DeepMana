"""Effect for Rokara (BAR_847).

Card Text: [x]<b>Rush</b>
After a friendly minion
attacks and survives,
give it +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1