"""Effect for Swinetusk Shank (BAR_322).

Card Text: [x]After you play a Poison,
 gain +1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1