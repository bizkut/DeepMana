"""Effect for Gigantotem (REV_838).

Card Text: Costs (1) less for each Totem you've summoned this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_838t")