"""Effect for Mind Control (VAN_CS1_113).

Card Text: Take control of an enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass