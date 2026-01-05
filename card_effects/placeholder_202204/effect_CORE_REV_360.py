"""Effect for Spirit Poacher (CORE_REV_360).

Card Text: <b>Battlecry:</b> Summon a random <b>Dormant</b> Wildseed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_360t")