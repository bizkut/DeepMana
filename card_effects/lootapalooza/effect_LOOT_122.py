"""Effect for Corrosive Sludge (LOOT_122).

Card Text: <b>Battlecry:</b> Destroy your opponent's weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()