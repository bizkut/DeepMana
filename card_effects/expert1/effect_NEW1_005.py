"""Effect for Kidnapper (NEW1_005).

Card Text: <b>Combo:</b> Return a minion to its owner's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass