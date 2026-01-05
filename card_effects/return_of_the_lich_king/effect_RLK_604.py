"""Effect for Thori'belore (RLK_604).

Card Text: [x]<b>Rush</b>. <b>Deathrattle:</b> Go
<b>Dormant</b>. Cast a Fire spell
to revive Thori'belore!
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass