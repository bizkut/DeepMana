"""Effect for Gnawing Greenfin (EDR_999).

Card Text: <b>Battlecry:</b> Get a
random Murloc.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass