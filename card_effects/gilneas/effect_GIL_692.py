"""Effect for Genn Greymane (GIL_692).

Card Text: [x]<b>Start of Game:</b>
If your deck has only even-
Cost cards, your starting
Hero Power costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass