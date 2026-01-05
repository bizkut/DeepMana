"""Effect for Toki, Time-Tinker (GIL_549).

Card Text: [x]<b>Battlecry:</b> Add a random
<b>Legendary</b> minion from
the past to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass