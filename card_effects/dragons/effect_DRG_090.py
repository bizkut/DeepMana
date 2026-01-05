"""Effect for Murozond the Infinite (DRG_090).

Card Text: <b>Battlecry:</b> Play all cards your opponent played last turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass