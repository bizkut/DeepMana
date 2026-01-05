"""Effect for Geosculptor Yip (LOOT_519).

Card Text: At the end of your turn, summon a random minion with Cost equal to your Armor <i>(up to 10)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_519t")