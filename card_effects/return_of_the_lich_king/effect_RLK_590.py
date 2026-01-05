"""Effect for The Sunwell (RLK_590).

Card Text: Fill your hand with random spells. Costs (1) less for each other card in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass