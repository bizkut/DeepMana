"""Effect for Azerite Elemental (DAL_548).

Card Text: At the start of your turn, gain <b>Spell Damage +2</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2