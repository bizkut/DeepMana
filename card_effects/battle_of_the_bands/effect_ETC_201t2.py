"""Effect for Bunch of Bananas (ETC_201t2).

Card Text: Give a minion +1/+1. <i>(Last Banana!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
