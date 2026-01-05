"""Effect for Command the Illidari (BT_173).

Card Text: Summon six 1/1 Illidari with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_173t")