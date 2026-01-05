"""Effect for Kael'thas Sinstrider (REV_021).

Card Text: Every third minion you play each turn costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass