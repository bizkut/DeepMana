"""Effect for Cavalry Horn (AV_341).

Card Text: <b>Deathrattle:</b> Summon the lowest Cost minion in your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_341t")