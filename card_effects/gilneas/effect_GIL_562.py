"""Effect for Vilebrood Skitterer (GIL_562).

Card Text: <b>Poisonous</b>
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass