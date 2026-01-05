"""Effect for Time Out! (TRL_302).

Card Text: Your hero is <b>Immune</b> until your next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass