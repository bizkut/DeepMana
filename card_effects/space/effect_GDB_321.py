"""Effect for Mutating Lifeform (GDB_321).

Card Text: After this survives damage, gain a random <b>Bonus Effect</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
