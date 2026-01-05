"""Effect for Trade Prince Gallywix (GVG_028).

Card Text: Whenever your opponent casts a spell, gain a copy of it and give them a Coin.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1