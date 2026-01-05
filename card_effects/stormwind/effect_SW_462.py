"""Effect for Hot Streak (SW_462).

Card Text: Your next Fire spell this turn costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass