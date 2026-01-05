"""Effect for Tome of Intellect (EX1_180).

Card Text: Add a random Mage spell to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass