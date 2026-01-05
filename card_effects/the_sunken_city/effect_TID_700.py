"""Effect for Disarming Elemental (TID_700).

Card Text: [x]<b>Battlecry:</b> <b>Dredge</b> for
your opponent. Set its
Cost to (6).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass