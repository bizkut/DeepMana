"""Effect for Air Raid (YOD_012).

Card Text: <b>Twinspell</b>
Summon two 1/1 Silver Hand Recruits with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_012t")