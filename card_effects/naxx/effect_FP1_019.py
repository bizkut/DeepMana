"""Effect for Poison Seeds (FP1_019).

Card Text: Destroy all minions and summon 2/2 Treants to replace them.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "FP1_019t")