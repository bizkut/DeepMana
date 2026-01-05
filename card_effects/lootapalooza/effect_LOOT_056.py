"""Effect for Astral Tiger (LOOT_056).

Card Text: <b>Deathrattle:</b> Shuffle a
 copy of this minion into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass