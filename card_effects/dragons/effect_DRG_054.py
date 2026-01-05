"""Effect for Big Ol' Whelp (DRG_054).

Card Text: <b>Battlecry:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)