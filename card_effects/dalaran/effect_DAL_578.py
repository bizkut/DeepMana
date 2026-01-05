"""Effect for Power of Creation (DAL_578).

Card Text: <b>Discover</b> a 6-Cost minion. Summon two copies of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_578t")