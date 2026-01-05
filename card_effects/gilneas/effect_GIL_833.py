"""Effect for Forest Guide (GIL_833).

Card Text: At the end of your turn, both players draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)