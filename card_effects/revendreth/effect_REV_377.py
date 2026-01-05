"""Effect for Invitation Courier (REV_377).

Card Text: After a card is added to your hand from another class, copy it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass