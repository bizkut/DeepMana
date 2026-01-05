"""Effect for Shimmering Tempest (UNG_846).

Card Text: <b>Battlecry:</b> Add a random Mage spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass