"""Effect for Zerek, Master Cloner (BOT_258).

Card Text: <b>Deathrattle:</b> If you've cast any spells on this minion, resummon it.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_258t")