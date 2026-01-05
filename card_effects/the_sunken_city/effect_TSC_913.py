"""Effect for Azsharan Trident (TSC_913).

Card Text: [x]<b>Deathrattle:</b> Put
a 'Sunken Trident' on the
 bottom of your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass