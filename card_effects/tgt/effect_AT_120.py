"""Effect for Frost Giant (AT_120).

Card Text: Costs (1) less for each time you used your Hero Power this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass