"""Effect for Rend Blackhand (BRM_029).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, destroy a <b>Legendary</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()