"""Effect for Wolfrider (CS2_124).

Card Text: <b>Charge</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass