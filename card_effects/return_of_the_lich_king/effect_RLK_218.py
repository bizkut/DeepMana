"""Effect for Silvermoon Arcanist (RLK_218).

Card Text: [x]<b>Spell Damage +2</b>
<b>Battlecry:</b> Your spells can’t
target heroes this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2