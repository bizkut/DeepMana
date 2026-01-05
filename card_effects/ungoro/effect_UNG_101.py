"""Effect for Shellshifter (UNG_101).

Card Text: [x]<b>Choose One - </b>Transform
into a 5/3 with <b>Stealth</b>;
or a 3/5 with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass