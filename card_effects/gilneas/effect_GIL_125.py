"""Effect for Mad Hatter (GIL_125).

Card Text: [x]<b>Battlecry:</b> Randomly toss
3 hats to other minions.
Each hat gives +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3