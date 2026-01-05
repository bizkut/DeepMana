"""Effect for Vex Crow (GIL_664).

Card Text: Whenever you cast a spell, summon a random
2-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_664t")