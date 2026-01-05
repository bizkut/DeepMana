"""Effect for Lady Liadrin (BT_334).

Card Text: [x]<b>Battlecry:</b> Add a copy of
each spell you cast on
friendly characters this
game to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass