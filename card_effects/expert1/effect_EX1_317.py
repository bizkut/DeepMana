"""Effect for Sense Demons (EX1_317).

Card Text: Draw 2 Demons
from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)