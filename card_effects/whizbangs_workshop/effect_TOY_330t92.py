"""Effect for Recursive Module (TOY_330t92).

Card Text: [x]<b>Deathrattle:</b> Shuffle this into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent
    pass
