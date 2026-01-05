"""Effect for Light of the Phoenix (RLK_603).

Card Text: Draw 2 cards. Costs (1) less for each damaged friendly character.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)