"""Effect for Siege Engine (GVG_086).

Card Text: Whenever you gain Armor, give this minion +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1