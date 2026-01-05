"""Effect for Circadiamancer (TIME_102).

Card Text: [x]<b>Battlecry:</b> Add a random
8-Cost minion to your hand.
At the start of your turns,
reduce its Cost by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass