"""Effect for Ambush (BT_707).

Card Text: [x]<b>Secret:</b> After your
opponent plays a minion,
summon a 2/3 Ambusher
with <b>Poisonous</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_707t")