"""Effect for Shifter Zerus (OG_123).

Card Text: Each turn this is in your hand, transform it into a random minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass