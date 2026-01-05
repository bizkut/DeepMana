"""Effect for Twilight Acolyte (LOOT_528).

Card Text: <b>Battlecry:</b> If you're holding
a Dragon, swap this minion's Attack with another minion's.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass