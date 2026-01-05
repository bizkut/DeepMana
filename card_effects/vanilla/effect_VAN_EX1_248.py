"""Effect for Feral Spirit (VAN_EX1_248).

Card Text: Summon two 2/3 Spirit Wolves with <b>Taunt</b>. <b>Overload:</b> (2)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_EX1_248t")