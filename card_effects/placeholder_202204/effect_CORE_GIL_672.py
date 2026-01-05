"""Effect for Spectral Cutlass (CORE_GIL_672).

Card Text: [x]<b>Lifesteal</b>
Whenever you play a card
from another class,
gain +1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1