"""Effect for Story of Amara (TLC_835).

Card Text: Set your hero's
Health to 40.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 40, source)