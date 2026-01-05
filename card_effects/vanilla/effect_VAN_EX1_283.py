"""Effect for Frost Elemental (VAN_EX1_283).

Card Text: <b>Battlecry:</b> <b>Freeze</b> a character.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True