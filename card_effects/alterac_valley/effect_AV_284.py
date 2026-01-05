"""Effect for Balinda Stonehearth (AV_284).

Card Text: <b>Battlecry:</b> Draw 2 spells. Swap their Costs with this minion's stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)