"""Effect for Spirit Claws (CORE_KAR_063).

Card Text: [x]Has +2 Attack while you
have <b>Spell Damage</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2