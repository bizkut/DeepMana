"""Effect for Eyes in the Sky (TLC_521).

Card Text: [x]<b>Battlecry:</b> Look at 3
cards in your enemy's deck.
Pick one to put on top.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass