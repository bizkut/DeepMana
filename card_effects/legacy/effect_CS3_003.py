"""Effect for Felsoul Jailer (CS3_003).

Card Text: [x]<b>Battlecry:</b> Your opponent
discards a minion.
<b>Deathrattle:</b> Return it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass