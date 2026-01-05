"""Effect for Druid of the Saber (AT_042).

Card Text: [x]<b>Choose One -</b> Transform
into a 2/1 with <b>Charge</b>;
or a 3/2 with <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass