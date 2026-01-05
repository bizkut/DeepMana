"""Effect for Party Crasher (CORE_REV_370).

Card Text: [x]<b>Battlecry:</b> Choose an
enemy minion. Throw a
random minion from
your hand at it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass