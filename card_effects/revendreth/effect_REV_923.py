"""Effect for Muck Pools (REV_923).

Card Text: Transform a friendly minion into one that costs (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass