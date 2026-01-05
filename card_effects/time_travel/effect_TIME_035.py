"""Effect for Time Machine (TIME_035).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Get a random <b>Rewind</b> card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass