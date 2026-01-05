"""Effect for Zentimo (TRL_085).

Card Text: [x]Whenever you target a
minion with a spell, cast it
again on its neighbors.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass