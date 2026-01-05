"""Effect for Pilfer (EX1_182).

Card Text: Add a random card from another class to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass