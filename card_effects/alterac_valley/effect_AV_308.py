"""Effect for Grave Defiler (AV_308).

Card Text: <b>Battlecry:</b> Copy a Fel spell in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass