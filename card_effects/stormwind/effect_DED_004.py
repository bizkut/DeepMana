"""Effect for Blackwater Cutlass (DED_004).

Card Text: [x]<b>Tradeable</b>
After you <b>Trade</b> this,
reduce the Cost of a spell
in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass