"""Effect for Twig of the World Tree (LOOT_392).

Card Text: <b>Deathrattle:</b> Refresh your Mana Crystals.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass