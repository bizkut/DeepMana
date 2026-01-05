"""Effect for Kodo Mount (SW_432).

Card Text: Give a minion +4/+2 and <b>Rush</b>. When it dies, summon a Kodo.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_432t")