"""Effect for Catrina Muerte (CORE_DAL_721).

Card Text: At the end of your turn, resurrect another friendly Undead minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass