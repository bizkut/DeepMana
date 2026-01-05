"""Effect for Soul Mirror (BT_198).

Card Text: Summon copies of enemy minions. They attack their copies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_198t")