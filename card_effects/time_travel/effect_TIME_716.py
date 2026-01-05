"""Effect for Slow Motion (TIME_716).

Card Text: Your opponent's cards cost (1) more next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass