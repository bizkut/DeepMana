"""Effect for Underbelly Fence (DAL_714).

Card Text: [x]<b>Battlecry:</b> If you're holding
a card from another class,
 gain +1/+1 and <b><b>Rush</b>.</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1