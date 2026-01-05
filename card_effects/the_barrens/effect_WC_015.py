"""Effect for Water Moccasin (WC_015).

Card Text: [x]<b>Stealth</b>
Has <b>Poisonous</b> while you
 have no other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass