"""Effect for Bomb Wrangler (YOD_024).

Card Text: Whenever this minion takes damage, summon a 1/1 Boom Bot.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_024t")