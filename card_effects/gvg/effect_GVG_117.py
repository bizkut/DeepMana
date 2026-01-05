"""Effect for Gazlowe (GVG_117).

Card Text: Whenever you cast a 1-Cost spell, add a random Mech to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass