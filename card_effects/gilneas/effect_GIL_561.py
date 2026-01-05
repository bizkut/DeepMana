"""Effect for Blackwald Pixie (GIL_561).

Card Text: <b>Battlecry:</b> Refresh your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass