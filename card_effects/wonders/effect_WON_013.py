"""Effect for Rat Sensei (WON_013).

Card Text: <b>Battlecry and Deathrattle:</b> Add two 1/1 Turtles with <b>Taunt</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass