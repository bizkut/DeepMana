"""Effect for Whirling Zap-o-matic (GVG_037).

Card Text: <b>Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass