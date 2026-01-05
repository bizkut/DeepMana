"""Effect for Gilded Gargoyle (LOOT_534).

Card Text: <b>Deathrattle:</b> Add a Coin to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass