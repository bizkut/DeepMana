"""Effect for Drakkari Enchanter (ICC_901).

Card Text: Your end of turn effects trigger twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass