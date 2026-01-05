"""Effect for Silverfury Stalwart (RLK_602).

Card Text: <b>Rush</b>
<b>Elusive</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass