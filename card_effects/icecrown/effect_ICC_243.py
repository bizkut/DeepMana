"""Effect for Corpse Widow (ICC_243).

Card Text: Your <b>Deathrattle</b> cards cost (2) less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass