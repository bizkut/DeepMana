"""Effect for Imprisoned Vilefiend (BT_156).

Card Text: <b>Dormant</b> for 2 turns.
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass