"""Effect for Vanessa VanCleef (CORE_CS3_005).

Card Text: <b>Combo:</b> Add a copy of the last card your opponent played to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass