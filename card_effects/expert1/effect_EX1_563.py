"""Effect for Malygos (EX1_563).

Card Text: <b>Spell Damage +5</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5