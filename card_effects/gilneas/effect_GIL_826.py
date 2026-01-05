"""Effect for Baku the Mooneater (GIL_826).

Card Text: [x]<b>Start of Game:</b>
If your deck has only odd-
Cost cards, upgrade
your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass