"""Effect for Soot Spewer (WON_033).

Card Text: <b>Spell Damage +1</b>
<b>Battlecry:</b> If you control
another Mech, get a random Fire spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1