"""Effect for Gahz'rilla (GVG_049).

Card Text: Whenever this minion takes damage, double its Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass