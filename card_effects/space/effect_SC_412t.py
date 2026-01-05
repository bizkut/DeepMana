"""Effect for Hellbat (SC_412t).

Card Text: Your other minions have +2 Attack and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
