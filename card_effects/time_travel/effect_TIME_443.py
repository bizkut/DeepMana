"""Effect for Hounds of Fury (TIME_443).

Card Text: [x]Summon two 3/3
Demons. If your deck has
no minions, they attack
the lowest Health enemy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_443t")