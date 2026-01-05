"""Effect for Guard Duty (DINO_433).

Card Text: Summon a random
6, 4, and 2-Cost
<b>Taunt</b> minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_433t")