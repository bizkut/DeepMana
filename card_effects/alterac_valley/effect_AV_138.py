"""Effect for Grimtotem Bounty Hunter (AV_138).

Card Text: <b>Battlecry:</b> Destroy an enemy <b>Legendary</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()