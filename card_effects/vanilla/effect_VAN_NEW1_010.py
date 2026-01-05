"""Effect for Al'Akir the Windlord (VAN_NEW1_010).

Card Text: <b>Charge, Divine Shield, Taunt, Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass