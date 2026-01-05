"""Effect for Spawnpool Forager (BAR_751).

Card Text: <b>Deathrattle:</b> Summon a 1/1 Tinyfin.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_751t")