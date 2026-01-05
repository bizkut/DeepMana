"""Effect for Murmuring Elemental (LOOT_517).

Card Text: <b>Battlecry:</b> Your next <b>Battlecry</b> this turn triggers twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass