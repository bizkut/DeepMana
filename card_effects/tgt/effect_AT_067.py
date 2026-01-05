"""Effect for Magnataur Alpha (AT_067).

Card Text: Also damages the minions next to whomever
he attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass