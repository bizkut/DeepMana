"""Effect for Ornery Direhorn (UNG_925).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> <b>Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass