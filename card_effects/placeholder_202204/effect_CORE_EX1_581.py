"""Effect for Sap (CORE_EX1_581).

Card Text: Return an enemy minion to your opponent's hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass