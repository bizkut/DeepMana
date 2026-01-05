"""Effect for Timber Wolf (VAN_DS1_175).

Card Text: Your other Beasts have +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1