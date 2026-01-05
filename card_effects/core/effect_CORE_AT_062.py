"""Effect for Ball of Spiders (CORE_AT_062).

Card Text: Summon three 1/1 Webspinners
with "<b>Deathrattle:</b> Get
a random Beast."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_AT_062t")