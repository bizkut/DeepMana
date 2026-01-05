"""Effect for Seismopod (DINO_421).

Card Text: <b>Taunt</b>, <b>Elusive</b>
<b>Deathrattle:</b> Give all minions in your hand
and deck +3/+3.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3