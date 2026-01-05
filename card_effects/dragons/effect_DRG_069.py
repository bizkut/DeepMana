"""Effect for Platebreaker (DRG_069).

Card Text: <b>Battlecry:</b> Destroy your opponent's Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()