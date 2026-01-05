"""Effect for Neptulon the Tidehunter (TID_712).

Card Text: [x]<b>Colossal +2</b>, <b>Rush</b>, <b>Windfury</b>
Whenever Neptulon attacks,
if you control any Hands,
they attack instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2