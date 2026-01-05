"""Effect for Eureka! (BOT_099).

Card Text: Summon a copy of a random minion from your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_099t")