"""Effect for Knight of the Wild (WON_003).

Card Text: Costs (1) less for each Beast you've summoned this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_003t")