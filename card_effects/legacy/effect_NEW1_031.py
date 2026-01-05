"""Effect for Animal Companion (NEW1_031).

Card Text: Summon a random Beast Companion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NEW1_031t")