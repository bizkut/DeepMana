"""Effect for Tinyfin's Caravan (BAR_043).

Card Text: At the start of your turn, draw a Murloc.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)