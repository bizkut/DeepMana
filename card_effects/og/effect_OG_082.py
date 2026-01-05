"""Effect for Evolved Kobold (OG_082).

Card Text: <b>Spell Damage +2</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2