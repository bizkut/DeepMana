"""Effect for Kalimos, Primal Lord (UNG_211).

Card Text: [x]<b>Battlecry:</b> If you played an
Elemental last turn, cast an
Elemental Invocation.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass