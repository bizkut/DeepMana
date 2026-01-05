"""Effect for Cagematch Custodian (DMF_704).

Card Text: <b>Battlecry:</b> Draw a weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)