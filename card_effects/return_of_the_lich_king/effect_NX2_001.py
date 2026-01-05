"""Effect for Tear Reality (NX2_001).

Card Text: [x]Add 2 random
Mage spells from the
past to your hand.
They cost (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass