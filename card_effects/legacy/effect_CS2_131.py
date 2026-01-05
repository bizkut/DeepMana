"""Effect for Stormwind Knight (CS2_131).

Card Text: <b>Charge</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass