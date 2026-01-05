"""Effect for Clockwork Giant (GVG_121).

Card Text: Costs (1) less for each card in your opponent's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass