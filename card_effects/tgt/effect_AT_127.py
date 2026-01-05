"""Effect for Nexus-Champion Saraad (AT_127).

Card Text: <b>Inspire:</b> Add a random spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass