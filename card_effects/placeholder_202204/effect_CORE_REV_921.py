"""Effect for The Stonewright (CORE_REV_921).

Card Text: <b>Battlecry:</b> For the rest of the game, your Totems have +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2