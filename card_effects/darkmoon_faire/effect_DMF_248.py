"""Effect for Felsteel Executioner (DMF_248).

Card Text: <b>Corrupt:</b> Become a weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass