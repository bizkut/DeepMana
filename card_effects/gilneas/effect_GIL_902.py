"""Effect for Cutthroat Buccaneer (GIL_902).

Card Text: <b>Combo:</b> Give your weapon +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1