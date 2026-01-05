"""Effect for Niri of the Crater (TLC_836).

Card Text: [x]Whenever you play a 1-Cost
minion, double its stats.
Whenever you cast a 1-Cost
spell, cast it twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass