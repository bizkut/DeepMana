"""Effect for Micro Mummy (ULD_217).

Card Text: [x]<b>Reborn</b>
At the end of your turn, give
another random friendly
minion +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1