"""Effect for Everburning Phoenix (FIR_919).

Card Text: [x]Costs (1) less for each card
you've played this turn.
<b>Deathrattle: </b>At end of turn,
get another Phoenix.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass