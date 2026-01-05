"""Effect for Holomancer (BOT_280).

Card Text: After your opponent plays a minion, summon a 1/1 copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_280t")