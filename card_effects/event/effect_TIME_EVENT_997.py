"""Effect for Welcome Home! (TIME_EVENT_997).

Card Text: Reopen a location. Give it "<b>Deathrattle:</b> Summon a random
3-Cost minion."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_EVENT_997t")