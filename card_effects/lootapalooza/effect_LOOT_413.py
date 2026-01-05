"""Effect for Plated Beetle (LOOT_413).

Card Text: <b>Deathrattle:</b> Gain 3 Armor.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(3)