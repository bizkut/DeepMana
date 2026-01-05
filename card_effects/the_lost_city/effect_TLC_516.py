"""Effect for Neferset Weaponsmith (TLC_516).

Card Text: [x]<b>Battlecry:</b> Get a random
weapon from another class.
<b>Combo:</b> Give it +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2