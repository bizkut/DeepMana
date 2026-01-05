"""Effect for Bloodsail Flybooter (DRG_035).

Card Text: <b>Battlecry:</b> Add two 1/1 Pirates to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass