"""Effect for Ysiel Windsinger (BT_131).

Card Text: Your spells cost (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass