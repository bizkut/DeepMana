"""Effect for Weaponized Piñata (BOT_401).

Card Text: <b>Deathrattle:</b> Add a random <b>Legendary</b> minion to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass