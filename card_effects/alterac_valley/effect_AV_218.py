"""Effect for Mass Polymorph (AV_218).

Card Text: Transform all minions into 1/1 Sheep.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass