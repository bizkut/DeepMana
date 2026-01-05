"""Effect for Gangplank Diver (TSC_007).

Card Text: <b>Dormant</b> for 1 turn.
<b>Rush</b>. <b>Immune</b> while attacking.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass