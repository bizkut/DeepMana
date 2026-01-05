"""Effect for Faceless Summoner (OG_207).

Card Text: <b>Battlecry:</b> Summon a random 3-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_207t")