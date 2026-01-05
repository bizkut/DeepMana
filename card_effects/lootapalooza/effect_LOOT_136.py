"""Effect for Sneaky Devil (LOOT_136).

Card Text: <b>Stealth</b>
Your other minions have +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1