"""Effect for Clockwork Assistant (VAC_464t11).

Card Text: Has +1/+1 for each spell you've cast this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
