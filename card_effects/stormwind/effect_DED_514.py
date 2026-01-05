"""Effect for Copycat (DED_514).

Card Text: <b>Battlecry:</b> Add a copy of the next card your opponent plays to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass