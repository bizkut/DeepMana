"""Effect for Insight (DMF_054).

Card Text: Draw a minion. <b>Corrupt:</b> Reduce its Cost by (2).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)