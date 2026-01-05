"""Effect for Ball of Spiders (WON_021).

Card Text: Summon three 1/1 Webspinners
with "<b>Deathrattle:</b> Get
a random Beast."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_021t")