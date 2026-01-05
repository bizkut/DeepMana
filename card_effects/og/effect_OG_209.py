"""Effect for Hallazeal the Ascended (OG_209).

Card Text: <b>Spell Damage +1</b>
Your spells have <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1