"""Effect for Slimescale Diver (TSC_013).

Card Text: <b>Dormant</b> for 1 turn.
<b>Rush</b>, <b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass