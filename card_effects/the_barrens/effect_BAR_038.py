"""Effect for Tavish Stormpike (BAR_038).

Card Text: After a friendly Beast attacks, summon a Beast from your deck that costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_038t")