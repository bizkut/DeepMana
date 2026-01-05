"""Effect for Arcane Watcher (DAL_434).

Card Text: Can't attack unless you have <b>Spell Damage</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass