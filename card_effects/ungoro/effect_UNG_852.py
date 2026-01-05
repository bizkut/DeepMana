"""Effect for Tyrantus (UNG_852).

Card Text: <b>Taunt</b>
<b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass