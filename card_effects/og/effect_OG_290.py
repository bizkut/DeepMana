"""Effect for Ancient Harbinger (OG_290).

Card Text: At the start of your turn, put a 10-Cost minion from your deck into your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass