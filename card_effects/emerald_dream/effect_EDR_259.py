"""Effect for Ursol (EDR_259).

Card Text: [x]<b>Battlecry:</b> Cast the highest
Cost spell from your hand as
 an Aura that lasts 3 turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass