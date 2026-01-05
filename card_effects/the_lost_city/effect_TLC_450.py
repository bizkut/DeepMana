"""Effect for Spelunker (TLC_450).

Card Text: <b>Battlecry:</b> Your next <b>Temporary</b> card costs
(2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass