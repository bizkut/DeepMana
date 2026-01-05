"""Effect for Rebuke (GIL_203).

Card Text: Enemy spells cost (5) more next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass