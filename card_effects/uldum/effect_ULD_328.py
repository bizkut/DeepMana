"""Effect for Clever Disguise (ULD_328).

Card Text: Add 2 random spells from another class to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass