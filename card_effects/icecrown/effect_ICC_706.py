"""Effect for Nerubian Unraveler (ICC_706).

Card Text: Spells cost (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass