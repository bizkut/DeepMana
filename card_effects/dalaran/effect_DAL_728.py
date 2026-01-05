"""Effect for Daring Escape (DAL_728).

Card Text: Return all friendly minions to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass