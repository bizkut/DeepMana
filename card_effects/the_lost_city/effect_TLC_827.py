"""Effect for Grazing Stegodon (TLC_827).

Card Text: At the end of your turn, gain +1 Attack <i>(even while in hand or deck)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1