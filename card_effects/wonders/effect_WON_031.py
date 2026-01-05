"""Effect for Mana Wyrm (WON_031).

Card Text: Whenever you cast a spell, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1