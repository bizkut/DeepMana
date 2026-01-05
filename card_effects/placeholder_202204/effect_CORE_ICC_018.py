"""Effect for Phantom Freebooter (CORE_ICC_018).

Card Text: <b>Battlecry:</b> Gain stats equal to your weapon's.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass