"""Effect for Babbling Book (CORE_KAR_009).

Card Text: <b>Battlecry:</b> Add a random Mage spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass