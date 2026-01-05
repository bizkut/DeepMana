"""Effect for The Rat King (SW_323).

Card Text: [x]<b>Rush</b>. <b>Deathrattle:</b> Go
<b>Dormant</b>. Revive after 5
friendly minions die.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass