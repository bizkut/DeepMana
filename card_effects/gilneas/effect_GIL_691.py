"""Effect for Archmage Arugal (GIL_691).

Card Text: Whenever you draw a minion, add a copy of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)