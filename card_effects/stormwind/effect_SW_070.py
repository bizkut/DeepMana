"""Effect for Mailbox Dancer (SW_070).

Card Text: [x]<b>Battlecry:</b> Add a Coin
to your hand.
<b>Deathrattle:</b> Give your
opponent one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1


def deathrattle(game, source):
    pass