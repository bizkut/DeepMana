"""Effect for Lotus Illusionist (CFM_697).

Card Text: [x]After this minion attacks
a hero, transform it into a
 random 6-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass