"""Effect for Expired Merchant (ULD_163).

Card Text: [x]<b>Battlecry:</b> Discard your
highest Cost card.
<b>Deathrattle:</b> Add 2 copies
of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass