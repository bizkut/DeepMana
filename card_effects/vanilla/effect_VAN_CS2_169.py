"""Effect for Young Dragonhawk (VAN_CS2_169).

Card Text: <b>Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass