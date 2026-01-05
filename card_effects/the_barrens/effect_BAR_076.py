"""Effect for Mor'shan Watch Post (BAR_076).

Card Text: [x]Can't attack. After your
opponent plays a minion,
 summon a 2/2 Grunt.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_076t")