"""Effect for Magnifying Glaive (CORE_REV_509).

Card Text: [x]After your hero attacks,
draw until you have
3 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)