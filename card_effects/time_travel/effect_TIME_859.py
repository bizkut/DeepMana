"""Effect for Anomalize (TIME_859).

Card Text: Summon a random
10 and 1-Cost minion. Scramble their stats.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_859t")