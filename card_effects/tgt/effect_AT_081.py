"""Effect for Eadric the Pure (AT_081).

Card Text: <b>Battlecry:</b> Change all enemy minions'
Attack to 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass