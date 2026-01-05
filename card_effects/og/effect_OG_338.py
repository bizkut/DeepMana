"""Effect for Nat, the Darkfisher (OG_338).

Card Text: At the start of your opponent's turn, they have a 50% chance to draw an extra card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(50)