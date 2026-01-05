"""Effect for Echo of Medivh (GVG_005).

Card Text: Put a copy of each friendly minion into your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass