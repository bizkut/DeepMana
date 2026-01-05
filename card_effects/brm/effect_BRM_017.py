"""Effect for Resurrect (BRM_017).

Card Text: Summon a random friendly minion that died this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BRM_017t")