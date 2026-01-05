"""Effect for Eaglehorn Bow (EX1_536).

Card Text: [x]Whenever a friendly
<b>Secret</b> is revealed,
gain +1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1