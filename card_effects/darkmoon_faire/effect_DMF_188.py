"""Effect for Y'Shaarj, the Defiler (DMF_188).

Card Text: [x]<b>Battlecry:</b> Add a copy of each
<b>Corrupted</b> card you've played
this game to your hand.
They cost (0) this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass