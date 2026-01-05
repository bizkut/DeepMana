"""Effect for Merithra (EDR_238).

Card Text: [x]<b>Battlecry:</b> Resurrect all
different friendly minions
that cost (8) or more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass