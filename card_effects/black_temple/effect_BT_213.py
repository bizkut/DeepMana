"""Effect for Scavenger's Ingenuity (BT_213).

Card Text: Draw a Beast.
Give it +3/+3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)