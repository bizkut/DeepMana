"""Effect for Ysera the Dreamer (CS3_033).

Card Text: <b>Battlecry:</b> Add one of each Dream card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass