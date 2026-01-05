"""Effect for Piloted Reaper (BOT_267).

Card Text: <b>Deathrattle:</b> Summon a random minion from
your hand that costs (2) or less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_267t")