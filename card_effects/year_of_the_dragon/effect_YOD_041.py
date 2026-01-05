"""Effect for Eye of the Storm (YOD_041).

Card Text: Summon three 5/6 Elementals with <b>Taunt</b>. <b>Overload:</b> (3)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_041t")