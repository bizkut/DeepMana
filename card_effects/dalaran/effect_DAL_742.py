"""Effect for Whirlwind Tempest (DAL_742).

Card Text: Your minions with <b>Windfury</b> have <b>Mega-Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass