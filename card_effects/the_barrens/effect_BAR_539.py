"""Effect for Celestial Alignment (BAR_539).

Card Text: Set your Mana Crystals to 0. Set the Cost of cards in your hand and deck to (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass