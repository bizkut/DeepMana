"""Effect for Lady Prestor (SW_078).

Card Text: [x]<b>Battlecry:</b> Transform minions
in your deck into random
Dragons. <i>(They keep their
  original stats and Cost.)</I>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass