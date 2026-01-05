"""Effect for Razorglaive Sentinel (ONY_036).

Card Text: After you play the left or right-most card in your hand, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)