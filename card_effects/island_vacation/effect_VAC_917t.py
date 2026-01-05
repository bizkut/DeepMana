"""Effect for Sunscreen (VAC_917t).

Card Text: Give a minion +1/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
