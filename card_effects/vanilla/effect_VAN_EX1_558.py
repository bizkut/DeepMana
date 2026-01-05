"""Effect for Harrison Jones (VAN_EX1_558).

Card Text: <b>Battlecry:</b> Destroy your opponent's weapon and draw cards equal to its Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)