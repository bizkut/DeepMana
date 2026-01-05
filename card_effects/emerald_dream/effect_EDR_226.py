"""Effect for Exotic Houndmaster (EDR_226).

Card Text: <b>Battlecry:</b> Draw a Beast. <b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)