"""Effect for Nagrand Slam (BT_163).

Card Text: Summon four 3/5 Clefthoofs that attack random enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_163t")