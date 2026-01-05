"""Effect for Unite the Murlocs (UNG_942).

Card Text: [x]<b>Quest:</b> Summon
8 Murlocs.
<b>Reward:</b> Megafin.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_942t")