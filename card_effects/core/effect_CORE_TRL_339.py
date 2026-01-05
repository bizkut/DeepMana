"""Effect for Master's Call (CORE_TRL_339).

Card Text: <b>Discover</b> a minion from your deck. If all
3 are Beasts, draw
them all instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)