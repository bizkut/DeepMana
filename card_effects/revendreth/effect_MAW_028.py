"""Effect for Mawsworn Bailiff (MAW_028).

Card Text: <b><b>Taunt</b>.</b> <b>Battlecry:</b> If you have 4 or more Armor, gain +4/+4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4