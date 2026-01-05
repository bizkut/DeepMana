"""Effect for Hunting Mastiff (GIL_607t).

Card Text: <b>Echo</b>
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass