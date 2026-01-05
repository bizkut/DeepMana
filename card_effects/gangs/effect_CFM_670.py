"""Effect for Mayor Noggenfogger (CFM_670).

Card Text: All targets are chosen randomly.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass