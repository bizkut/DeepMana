"""Effect for Gigafin (TSC_962).

Card Text: [x]<b>Colossal +1</b>. <b>Battlecry:</b>
Devour all enemy minions.
<b>Deathrattle:</b> Spit them
back out.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1


def deathrattle(game, source):
    pass