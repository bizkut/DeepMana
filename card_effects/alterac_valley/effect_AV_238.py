"""Effect for Gankster (AV_238).

Card Text: [x]<b>Stealth</b>
After your opponent plays
a minion, attack it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass