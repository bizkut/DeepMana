"""Effect for Silverware Golem (KAR_205).

Card Text: If you discard this minion, summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_205t")