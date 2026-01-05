"""Effect for Toothy Chest (LOOT_134).

Card Text: At the start of your turn, set this minion's Attack to 4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass