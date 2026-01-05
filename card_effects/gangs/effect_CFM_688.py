"""Effect for Spiked Hogrider (CFM_688).

Card Text: <b>Battlecry:</b> If an enemy minion has <b>Taunt</b>, gain <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass