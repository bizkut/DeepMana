"""Effect for Shady Dealer (AT_032).

Card Text: <b>Battlecry:</b> If you have a Pirate, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1