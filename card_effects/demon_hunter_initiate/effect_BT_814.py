"""Effect for Illidari Felblade (BT_814).

Card Text: <b>Rush</b>
<b>Outcast:</b> Gain <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass