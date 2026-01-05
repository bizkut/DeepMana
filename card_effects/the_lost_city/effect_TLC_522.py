"""Effect for Opu the Unseen (TLC_522).

Card Text: <b><b>Stealth</b>.</b> <b>Battlecry, Combo,
and Deathrattle:</b> Cast
'Fan of Knives'.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass