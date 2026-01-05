"""Effect for Conjure Mana Biscuit (YOP_019).

Card Text: Add a Biscuit to your hand that refreshes 2 Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass