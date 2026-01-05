"""Effect for Faerie Dragon (VAN_NEW1_023).

Card Text: <b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass