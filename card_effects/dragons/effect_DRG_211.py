"""Effect for Squallhunter (DRG_211).

Card Text: <b>Spell Damage +2</b>
<b>Overload:</b> (2)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2