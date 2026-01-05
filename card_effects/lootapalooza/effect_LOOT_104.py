"""Effect for Shifting Scroll (LOOT_104).

Card Text: Each turn this is in your hand, transform it into a random Mage spell.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass