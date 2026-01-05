"""Effect for Kobold Illusionist (LOOT_412).

Card Text: <b>Deathrattle:</b> Summon a 1/1 copy of a minion from your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_412t")