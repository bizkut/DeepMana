"""Effect for Linecracker (TRL_528).

Card Text: <b>Overkill:</b> Double this minion's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass