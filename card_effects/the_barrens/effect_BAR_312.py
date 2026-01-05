"""Effect for Soothsayer's Caravan (BAR_312).

Card Text: At the start of your turn, copy a spell from your opponent's deck to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass