"""Effect for Sanctum Chandler (SW_111).

Card Text: After you cast a Fire spell, draw a spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)