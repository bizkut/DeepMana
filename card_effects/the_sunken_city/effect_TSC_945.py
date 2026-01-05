"""Effect for Azsharan Saber (TSC_945).

Card Text: [x]<b><b>Rush</b>.</b> <b>Deathrattle:</b> Put a
'Sunken Saber' on the
bottom of your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass