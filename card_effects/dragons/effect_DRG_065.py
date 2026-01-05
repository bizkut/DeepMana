"""Effect for Hippogryph (DRG_065).

Card Text: <b>Rush</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass