"""Effect for Jungle Giants (UNG_116).

Card Text: [x]<b>Quest:</b> Summon
4 minions with
5 or more Attack.
<b>Reward:</b> Barnabus.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_116t")