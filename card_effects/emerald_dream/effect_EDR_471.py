"""Effect for Tortolla (EDR_471).

Card Text: [x]<b>Taunt</b>, <b>Elusive</b>
After this takes damage,
gain 1 Armor and give
this minion +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1