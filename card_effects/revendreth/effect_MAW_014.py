"""Effect for Prosecutor Mel'tranix (MAW_014).

Card Text: [x]<b>Battlecry:</b> Your opponent
can only play their left- 
and right-most cards on 
their next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass