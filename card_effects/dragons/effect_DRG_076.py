"""Effect for Faceless Corruptor (DRG_076).

Card Text: [x]<b>Rush</b>. <b>Battlecry:</b> Transform
one of your minions into
a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass