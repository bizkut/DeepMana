"""Effect for Genzo, the Shark (CFM_808).

Card Text: Whenever this attacks, both players draw until they have 3 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)