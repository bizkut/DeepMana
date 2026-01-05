"""Effect for Troublemaker (SCH_337).

Card Text: At the end of your turn, summon two 3/3 Ruffians that attack random enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_337t")