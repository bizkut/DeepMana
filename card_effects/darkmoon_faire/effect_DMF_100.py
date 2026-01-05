"""Effect for Confection Cyclone (DMF_100).

Card Text: <b>Battlecry:</b> Add two 1/2 Sugar Elementals to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass