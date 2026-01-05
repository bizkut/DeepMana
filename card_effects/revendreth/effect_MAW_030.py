"""Effect for Torghast Custodian (MAW_030).

Card Text: [x]<b>Battlecry:</b> For each
enemy minion, randomly
gain <b>Rush</b>, <b>Divine Shield</b>,
or <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass