"""Effect for Northshire Farmer (SW_064).

Card Text: <b>Battlecry:</b> Choose a friendly Beast. Shuffle three 3/3 copies into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass