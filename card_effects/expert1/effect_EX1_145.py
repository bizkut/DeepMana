"""Effect for Preparation (EX1_145).

Card Text: The next spell you cast this turn costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass