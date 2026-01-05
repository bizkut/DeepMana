"""Effect for Coordinated Strike (CORE_BT_036).

Card Text: Summon three 1/1 Illidari with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_BT_036t")