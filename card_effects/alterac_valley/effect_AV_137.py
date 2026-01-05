"""Effect for Irondeep Trogg (AV_137).

Card Text: [x]After your opponent
casts a spell, summon
 another Irondeep Trogg.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_137t")