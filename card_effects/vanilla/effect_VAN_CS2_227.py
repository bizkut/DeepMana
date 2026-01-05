"""Effect for Venture Co. Mercenary (VAN_CS2_227).

Card Text: Your minions cost (3) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass