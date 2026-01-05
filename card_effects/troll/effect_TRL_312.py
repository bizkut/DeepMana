"""Effect for Spellzerker (TRL_312).

Card Text: Has <b>Spell Damage +2</b> while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2