"""Effect for Captain Greenskin (NEW1_024).

Card Text: <b>Battlecry:</b> Give your weapon +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1