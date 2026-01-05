"""Effect for Thorngrowth Sentries (BAR_533).

Card Text: Summon two 1/2 Turtles with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_533t")