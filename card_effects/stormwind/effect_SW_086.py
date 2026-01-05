"""Effect for Shady Bartender (SW_086).

Card Text: <b>Tradeable</b>
<b>Battlecry:</b> Give your Demons +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2