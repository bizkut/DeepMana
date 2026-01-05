"""Effect for Rokara, the Valorous (AV_202).

Card Text: <b>Battlecry:</b> Equip a 5/2 Unstoppable Force.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass