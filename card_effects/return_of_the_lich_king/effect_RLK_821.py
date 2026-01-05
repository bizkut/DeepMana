"""Effect for Scourge Tamer (RLK_821).

Card Text: <b>Battlecry:</b> Craft a custom Zombeast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass