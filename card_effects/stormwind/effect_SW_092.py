"""Effect for Anetheron (SW_092).

Card Text: [x]Costs (1) if your hand is full.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass