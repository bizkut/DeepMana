"""Effect for Alara'shi (EDR_493).

Card Text: [x]<b>Battlecry:</b> Transform minions
in your hand into random
Demons. <i>(They keep their
  original stats and Cost.)</I>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass