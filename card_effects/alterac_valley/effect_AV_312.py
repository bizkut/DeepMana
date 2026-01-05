"""Effect for Sacrificial Summoner (AV_312).

Card Text: <b>Battlecry:</b> Destroy a friendly minion. Summon a minion from your deck that costs (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_312t")