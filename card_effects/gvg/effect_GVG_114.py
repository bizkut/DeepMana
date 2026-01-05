"""Effect for Sneed's Old Shredder (GVG_114).

Card Text: <b>Deathrattle:</b> Summon a random <b>Legendary</b> minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_114t")