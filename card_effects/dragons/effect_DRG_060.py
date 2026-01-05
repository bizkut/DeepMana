"""Effect for Fire Hawk (DRG_060).

Card Text: <b>Battlecry:</b> Gain +1 Attack for each card in your opponent's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1