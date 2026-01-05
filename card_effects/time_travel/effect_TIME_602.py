"""Effect for Wormhole (TIME_602).

Card Text: <b>Rewind</b>
Summon a random
3-Cost Beast. It attacks
a random enemy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_602t")