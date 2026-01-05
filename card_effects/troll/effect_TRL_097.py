"""Effect for Seance (TRL_097).

Card Text: Choose a minion. Add a copy of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass