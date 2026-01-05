"""Effect for Clownfish (TID_004).

Card Text: <b>Battlecry:</b> Your next two Murlocs cost (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass