"""Effect for Scalelord (YOD_043).

Card Text: <b>Battlecry:</b> Give your Murlocs <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1