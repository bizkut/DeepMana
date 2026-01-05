"""Effect for Stormforged Axe (VAN_EX1_247).

Card Text: <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass