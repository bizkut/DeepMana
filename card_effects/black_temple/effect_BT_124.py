"""Effect for Corsair Cache (BT_124).

Card Text: Draw a weapon.
Give it +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)