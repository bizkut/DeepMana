"""Effect for Voltaic Burst (BOT_451).

Card Text: Summon two 1/1 Sparks with <b>Rush</b>. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_451t")