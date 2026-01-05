"""Effect for Druid of the Reef (DED_001).

Card Text: [x]<b>Choose One - </b>Transform into
a 3/1 Shark with <b>Rush</b>; or
a 1/3 Turtle with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass