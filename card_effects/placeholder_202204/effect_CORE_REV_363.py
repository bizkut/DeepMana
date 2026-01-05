"""Effect for Ara'lon (CORE_REV_363).

Card Text: <b>Battlecry:</b> Summon one of each <b>Dormant</b> Wildseed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_363t")