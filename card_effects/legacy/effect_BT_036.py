"""Effect for Coordinated Strike (BT_036).

Card Text: Summon three 1/1 Illidari with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_036t")