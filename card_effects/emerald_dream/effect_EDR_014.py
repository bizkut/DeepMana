"""Effect for Verdant Dreamsaber (EDR_014).

Card Text: <b>Battlecry:</b> If this costs (3)
or less, attack two random enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass