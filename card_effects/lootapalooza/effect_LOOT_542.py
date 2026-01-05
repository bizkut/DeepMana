"""Effect for Kingsbane (LOOT_542).

Card Text: [x]Always keeps
enchantments.
<b>Deathrattle:</b> Shuffle this
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass