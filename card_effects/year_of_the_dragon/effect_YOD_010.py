"""Effect for Shotbot (YOD_010).

Card Text: <b>Reborn</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass