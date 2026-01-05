"""Effect for Ectomancy (BOT_521).

Card Text: Summon copies of all Demons you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_521t")