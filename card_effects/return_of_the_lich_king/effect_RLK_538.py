"""Effect for Devourer of Souls (RLK_538).

Card Text: After a friendly minion dies, gain its <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass