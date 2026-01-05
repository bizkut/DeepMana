"""Effect for Evasive Chimaera (DRG_066).

Card Text: <b>Poisonous</b>
<b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass