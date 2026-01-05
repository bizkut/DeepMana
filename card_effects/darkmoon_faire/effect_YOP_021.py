"""Effect for Imprisoned Phoenix (YOP_021).

Card Text: <b>Dormant</b> for 2 turns.
<b>Spell Damage +2</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2