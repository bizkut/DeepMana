"""Effect for Toshley (GVG_115).

Card Text: <b>Battlecry and Deathrattle:</b> Add a <b>Spare Part</b> card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass