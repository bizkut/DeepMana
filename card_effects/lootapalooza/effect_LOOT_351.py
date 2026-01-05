"""Effect for Greedy Sprite (LOOT_351).

Card Text: <b>Deathrattle:</b> Gain an empty Mana Crystal.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass