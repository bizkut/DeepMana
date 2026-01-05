"""Effect for Cult Sorcerer (OG_303).

Card Text: [x]<b><b>Spell Damage</b> +1</b>
After you cast a spell,
give your C'Thun +1/+1
<i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1