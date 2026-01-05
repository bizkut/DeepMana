"""Effect for Druid of the Scythe (GIL_188).

Card Text: [x]<b>Choose One -</b> Transform
into a 4/2 with <b>Rush</b>;
or a 2/4 with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass