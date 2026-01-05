"""Effect for EVIL Miscreant (DAL_415).

Card Text: <b>Combo:</b> Add two random <b>Lackeys</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass