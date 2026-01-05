"""Effect for Desert Camel (LOE_020).

Card Text: <b>Battlecry:</b> Put a 1-Cost minion from each deck into the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass