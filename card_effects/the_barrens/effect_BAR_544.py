"""Effect for Reckless Apprentice (BAR_544).

Card Text: <b>Battlecry:</b> Fire your Hero Power at all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass