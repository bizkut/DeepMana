"""Effect for Kel'Thuzad (FP1_013).

Card Text: At the end of each turn, summon all friendly minions that died this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "FP1_013t")