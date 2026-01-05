"""Effect for Glinda Crowskin (GIL_618).

Card Text: Minions in your hand have <b>Echo</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass