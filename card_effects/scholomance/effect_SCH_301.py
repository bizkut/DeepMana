"""Effect for Rune Dagger (SCH_301).

Card Text: After your hero attacks, gain <b>Spell Damage +1</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1