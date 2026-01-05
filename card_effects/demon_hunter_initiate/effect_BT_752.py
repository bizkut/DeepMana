"""Effect for Blur (BT_752).

Card Text: Your hero can't take damage this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass