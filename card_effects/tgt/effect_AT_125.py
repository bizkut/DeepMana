"""Effect for Icehowl (AT_125).

Card Text: <b>Charge</b>
Can't attack heroes.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass