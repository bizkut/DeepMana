"""Effect for RAFAAM LADDER!! (TIME_031).

Card Text: Draw 3 cards of different Costs.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)