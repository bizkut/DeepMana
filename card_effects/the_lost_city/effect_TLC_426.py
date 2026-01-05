"""Effect for Dive the Golakka Depths (TLC_426).

Card Text: <b>Repeatable Quest:</b> Summon 6 Murlocs.
<b>Reward:</b> Murlocs you summon gain +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_426t")