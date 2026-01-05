"""Effect for N'Zoth's First Mate (OG_312).

Card Text: <b>Battlecry:</b> Equip a 1/3 Rusty Hook.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass