"""Effect for Pelican Diver (TSC_647).

Card Text: <b>Dormant</b> for 1 turn.
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass