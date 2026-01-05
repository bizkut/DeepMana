"""Effect for Gadgetzan Ferryman (CFM_693).

Card Text: <b>Combo:</b> Return a friendly minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass