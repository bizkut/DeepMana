"""Effect for Nat Pagle (VAN_EX1_557).

Card Text: At the start of your turn, you have a 50% chance to draw an extra card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(50)