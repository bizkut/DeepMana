"""Effect for Totem Golem (AT_052).

Card Text: <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass