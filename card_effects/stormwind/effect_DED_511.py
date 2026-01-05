"""Effect for Suckerhook (DED_511).

Card Text: [x]At the end of your turn,
transform your weapon into
one that costs (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass