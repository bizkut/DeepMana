"""Effect for Trenchstalker (TSC_659).

Card Text: <b>Battlecry:</b> Attack three different random enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass