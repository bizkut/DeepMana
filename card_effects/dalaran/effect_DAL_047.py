"""Effect for Walking Fountain (DAL_047).

Card Text: <b>Lifesteal</b>, <b>Rush</b>, <b>Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass