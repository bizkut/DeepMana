"""Effect for Ritual Chopper (DRG_021).

Card Text: <b>Battlecry:</b> <b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass