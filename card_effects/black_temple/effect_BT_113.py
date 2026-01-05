"""Effect for Totemic Reflection (BT_113).

Card Text: Give a minion +2/+2.
If it's a Totem, summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_113t")