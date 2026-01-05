"""Effect for Drygulch Jailor (LOOT_363).

Card Text: <b>Deathrattle:</b> Add 3 Silver Hand Recruits to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass