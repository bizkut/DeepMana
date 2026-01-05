"""Effect for Warglaives of Azzinoth (CORE_BT_430).

Card Text: After attacking a minion, your hero may attack again.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass