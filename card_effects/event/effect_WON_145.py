"""Effect for Avatar of Hearthstone (WON_145).

Card Text: <b>Battlecry:</b> Open a Standard Pack. Play all cards from it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass