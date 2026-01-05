"""Effect for Mecharoo (BOT_445).

Card Text: <b>Deathrattle:</b> Summon a 1/1 Jo-E Bot.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_445t")