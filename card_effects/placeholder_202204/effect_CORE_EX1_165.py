"""Effect for Druid of the Claw (CORE_EX1_165).

Card Text: [x]<b>Choose One -</b> Transform
into a 7/6 with <b>Rush</b>;
or a 4/9 with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass