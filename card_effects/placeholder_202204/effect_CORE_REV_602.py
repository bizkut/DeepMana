"""Effect for Nightcloak Sanctum (CORE_REV_602).

Card Text: <b>Freeze</b> a minion. Summon a 2/2 Volatile Skeleton.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_602t")