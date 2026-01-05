"""Effect for Xaril, Poisoned Mind (OG_080).

Card Text: <b>Battlecry and Deathrattle:</b> Add a random Toxin card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass