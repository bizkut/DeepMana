"""Effect for Royal Informant (TIME_036).

Card Text: [x]<b>Battlecry:</b> Look at the right-
most card in your opponent's
hand. Either get a copy of it or
increase its Cost by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass