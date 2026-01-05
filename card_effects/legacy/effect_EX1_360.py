"""Effect for Humility (EX1_360).

Card Text: Change a minion's Attack to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass