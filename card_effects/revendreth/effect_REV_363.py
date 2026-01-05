"""Effect for Ara'lon (REV_363).

Card Text: <b>Battlecry:</b> Summon one of each <b>Dormant</b> Wildseed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_363t")