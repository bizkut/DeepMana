"""Effect for Envoy Rustwix (YOP_004).

Card Text: [x]<b>Deathrattle:</b> Shuffle 3
random Prime <b>Legendary</b>
minions into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass