"""Effect for Imprisoned Satyr (BT_127).

Card Text: [x]<b>Dormant</b> for 2 turns.
When this awakens, reduce
the Cost of a random minion
in your hand by (5).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass