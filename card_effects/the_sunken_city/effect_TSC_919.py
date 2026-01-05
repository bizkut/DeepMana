"""Effect for Azsharan Sentinel (TSC_919).

Card Text: [x]<b>Taunt</b>. <b>Deathrattle:</b> Put a
'Sunken Sentinel' on the
bottom of your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass