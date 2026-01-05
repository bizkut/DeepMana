"""Effect for Ursoc (EDR_819).

Card Text: <b>Battlecry:</b> Attack ALL
other minions.
<b>Deathrattle:</b> Resurrect any this killed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass