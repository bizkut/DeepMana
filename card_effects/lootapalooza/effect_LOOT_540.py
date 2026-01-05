"""Effect for Dragonhatcher (LOOT_540).

Card Text: At the end of your turn, <b>Recruit</b> a Dragon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass