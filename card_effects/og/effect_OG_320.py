"""Effect for Midnight Drake (OG_320).

Card Text: <b>Battlecry:</b> Gain +1 Attack for each other card
in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1