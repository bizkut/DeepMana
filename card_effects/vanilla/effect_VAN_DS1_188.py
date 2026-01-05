"""Effect for Gladiator's Longbow (VAN_DS1_188).

Card Text: Your hero is <b>Immune</b> while attacking.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass