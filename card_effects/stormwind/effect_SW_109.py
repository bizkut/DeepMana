"""Effect for Clumsy Courier (SW_109).

Card Text: <b>Battlecry:</b> Cast the highest Cost spell from your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass