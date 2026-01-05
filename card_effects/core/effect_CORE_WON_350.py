"""Effect for I Know a Guy (CORE_WON_350).

Card Text: <b>Discover</b> a <b>Taunt</b> minion. Give it +1/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
