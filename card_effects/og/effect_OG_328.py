"""Effect for Master of Evolution (OG_328).

Card Text: <b>Battlecry:</b> Transform a friendly minion into a random one that costs (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass