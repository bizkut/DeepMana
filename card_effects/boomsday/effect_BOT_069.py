"""Effect for The Boomship (BOT_069).

Card Text: Summon 3 random minions from your hand. Give them <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_069t")