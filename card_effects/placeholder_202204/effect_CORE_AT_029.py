"""Effect for Buccaneer (CORE_AT_029).

Card Text: Whenever you equip a weapon, give it +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1