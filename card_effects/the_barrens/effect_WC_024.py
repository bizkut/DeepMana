"""Effect for Man-at-Arms (WC_024).

Card Text: <b>Battlecry:</b> If you have a weapon equipped, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1