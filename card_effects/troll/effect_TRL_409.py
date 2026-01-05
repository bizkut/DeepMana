"""Effect for Gral, the Shark (TRL_409).

Card Text: [x]<b>Battlecry:</b> Eat a minion in
your deck and gain its stats.
<b>Deathrattle:</b> Add it to
your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass