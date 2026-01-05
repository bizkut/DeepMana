"""Effect for Overgrowth (BT_130).

Card Text: Gain two empty Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass