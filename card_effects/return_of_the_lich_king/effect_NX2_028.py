"""Effect for Hookfist-3000 (NX2_028).

Card Text: After your hero attacks, gain 4 Armor and
draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)