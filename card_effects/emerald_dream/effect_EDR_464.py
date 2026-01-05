"""Effect for Tyrande (EDR_464).

Card Text: <b>Battlecry:</b> The next 3 spells you play cast twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass