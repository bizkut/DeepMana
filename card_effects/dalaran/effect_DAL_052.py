"""Effect for Muckmorpher (DAL_052).

Card Text: [x]<b>Battlecry:</b> Transform into
a 4/4 copy of a different
minion in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass