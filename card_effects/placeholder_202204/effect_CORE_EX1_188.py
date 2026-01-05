"""Effect for Barrens Stablehand (CORE_EX1_188).

Card Text: <b>Battlecry:</b> Summon a random Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_EX1_188t")