"""Effect for Past Gnomeregan (TIME_044).

Card Text: [x]Give a minion +2/+1.
<i>Advance to the present!</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2