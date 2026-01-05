"""Effect for Bulwark of Azzinoth (CORE_BT_781).

Card Text: [x]Whenever your hero would
take damage, this loses
 1 Durability instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass