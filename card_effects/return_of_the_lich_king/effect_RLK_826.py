"""Effect for Silvermoon Farstrider (RLK_826).

Card Text: <b>Battlecry:</b> Give all
Arcane spells in your hand
<b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1