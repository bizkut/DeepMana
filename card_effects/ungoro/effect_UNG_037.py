"""Effect for Tortollan Shellraiser (UNG_037).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Give a random
 friendly minion +1/+1.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1