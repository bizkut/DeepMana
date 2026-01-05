"""Effect for Ixlid, Fungal Lord (LOOT_329).

Card Text: After you play a minion, summon a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_329t")