"""Effect for Anchored Totem (TSC_922).

Card Text: After you summon a 1-Cost minion, give it +2/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_922t")