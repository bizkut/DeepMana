"""Effect for Heir of Hereafter (TIME_871).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Gain +2/+2 for
each damaged minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2