"""Effect for Vicious Scalehide (GIL_143).

Card Text: <b>Lifesteal</b>
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass