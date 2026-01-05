"""Effect for Pterrorwing Ravager (TLC_366).

Card Text: <b>Rush</b>
<b>Kindred:</b> Costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass