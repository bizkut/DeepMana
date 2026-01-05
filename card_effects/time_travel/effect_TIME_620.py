"""Effect for Untimely Death (TIME_620).

Card Text: <b>Secret:</b> When a friendly minion dies the turn after being played, resummon it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_620t")