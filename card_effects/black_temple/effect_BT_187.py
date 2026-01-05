"""Effect for Kayn Sunfury (BT_187).

Card Text: <b>Charge</b>
All friendly attacks ignore <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass