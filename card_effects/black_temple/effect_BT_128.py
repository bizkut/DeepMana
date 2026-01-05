"""Effect for Fungal Fortunes (BT_128).

Card Text: Draw 3 cards. Discard any minions drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)