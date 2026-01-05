"""Effect for Radiance of Azshara (TSC_635).

Card Text: [x]<b>Fire Spell Damage +2</b>
Your Nature spells cost (1)
less. After you cast a Frost
spell, gain 3 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2