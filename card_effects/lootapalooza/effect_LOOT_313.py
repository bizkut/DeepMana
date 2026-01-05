"""Effect for Crystal Lion (LOOT_313).

Card Text: [x]<b>Divine Shield</b>
Costs (1) less for each Silver
Hand Recruit you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass