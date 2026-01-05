"""Effect for Cenarion Hold (WON_015).

Card Text: [x]Your next <b>Choose One</b>
card this turn has both
effects combined.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass