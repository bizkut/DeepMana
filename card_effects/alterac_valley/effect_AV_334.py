"""Effect for Stormpike Battle Ram (AV_334).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Your next
Beast costs (2) less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass