"""Effect for Face Collector (GIL_677).

Card Text: <b>Echo</b>
<b>Battlecry:</b> Add a random <b>Legendary</b> minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass