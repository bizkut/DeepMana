"""Effect for Hoarding Dragon (LOOT_144).

Card Text: <b>Deathrattle:</b> Give your opponent two Coins.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1