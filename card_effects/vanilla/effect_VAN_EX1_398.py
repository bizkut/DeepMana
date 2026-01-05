"""Effect for Arathi Weaponsmith (VAN_EX1_398).

Card Text: <b>Battlecry:</b> Equip a 2/2 weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass