"""Effect for Incriminating Psychic (MAW_022).

Card Text: [x]<b>Taunt</b>
 <b>Deathrattle:</b> Copy two
 random cards from your
opponent's hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass