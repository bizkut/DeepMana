"""Effect for Astral Communion (AT_043).

Card Text: Gain 10 Mana Crystals. Discard your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass