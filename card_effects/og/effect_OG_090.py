"""Effect for Cabalist's Tome (OG_090).

Card Text: Get 3 random
Mage spells.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass