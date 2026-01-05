"""Effect for Fizzy Elemental (DMF_059).

Card Text: <b>Rush</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass