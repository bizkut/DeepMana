"""Effect for Tiny Toys (SW_034).

Card Text: Summon four random 5-Cost minions.
Make them 2/2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_034t")