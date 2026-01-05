"""Effect for Coilfang Constrictor (TID_744).

Card Text: [x]<b>Battlecry:</b> Look at 3 cards
in your opponent's hand
 and choose one. It can't
be played next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass