"""Effect for Battleground Battlemaster (SW_063).

Card Text: Adjacent minions
have <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass