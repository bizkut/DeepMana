"""Effect for Dark Prophecy (YOD_015).

Card Text: <b>Discover</b> a 2-Cost minion. Summon it and give it +3 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_015t")