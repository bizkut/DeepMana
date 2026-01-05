"""Effect for Hoard Pillager (DRG_055).

Card Text: <b>Battlecry:</b> Equip one of your destroyed weapons.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()