"""Effect for Arch-Villain Rafaam (CORE_DAL_422).

Card Text: <b><b>Taunt</b>
Battlecry:</b> Replace your hand and deck with <b>Legendary</b> minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass