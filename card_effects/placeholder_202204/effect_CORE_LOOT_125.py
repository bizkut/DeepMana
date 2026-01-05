"""Effect for Stoneskin Basilisk (CORE_LOOT_125).

Card Text: <b>Divine Shield</b>
 <b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass