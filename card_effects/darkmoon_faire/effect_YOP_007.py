"""Effect for Dark Inquisitor Xanesh (YOP_007).

Card Text: [x]<b>Battlecry:</b> Reduce the
Cost of all <b>Corrupt</b> and
<b>Corrupted</b> cards in your
hand and deck by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass