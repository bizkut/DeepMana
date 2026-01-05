"""Effect for Grey Sage Parrot (DED_515).

Card Text: <b>Battlecry:</b> Repeat the last spell you've cast that costs (6) or more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass