"""Effect for Master Oakheart (LOOT_521).

Card Text: <b>Battlecry:</b> <b>Recruit</b> a 1, 2, and 3-Attack minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass