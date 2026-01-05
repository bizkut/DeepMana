"""Effect for Hir'eek, the Bat (TRL_253).

Card Text: <b>Battlecry:</b> Fill your board with copies of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass