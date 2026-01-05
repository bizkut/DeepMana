"""Effect for Darkspeaker (OG_102).

Card Text: <b>Battlecry:</b> Swap stats with a friendly minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass