"""Effect for Shrieking Shroom (LOOT_394).

Card Text: At the end of your turn, summon a random
1-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_394t")