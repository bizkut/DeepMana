"""Effect for Soridormi (WON_146).

Card Text: [x]<b>Dormant</b> for 2 turns.
When this awakens, reduce
the Cost of all Dragons
in your hand by (4).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass