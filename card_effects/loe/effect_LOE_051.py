"""Effect for Jungle Moonkin (LOE_051).

Card Text: Both players have
<b>Spell Damage +2</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2