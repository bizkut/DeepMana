"""Effect for Power Word: Replicate (BOT_529).

Card Text: Choose a friendly minion. Summon a 5/5 copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_529t")