"""Effect for Spirit of the Tides (TID_000).

Card Text: [x]If you have any unspent
Mana at the end of
 your turn, gain +1/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1