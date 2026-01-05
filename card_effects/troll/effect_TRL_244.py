"""Effect for Predatory Instincts (TRL_244).

Card Text: [x]Draw a Beast from your
deck. Double its Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)