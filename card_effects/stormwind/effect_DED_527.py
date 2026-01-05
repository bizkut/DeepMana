"""Effect for Blacksmithing Hammer (DED_527).

Card Text: [x]<b>Tradeable</b>
After you <b>Trade</b> this,
 gain +2 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2