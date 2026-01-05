"""Effect for Hemet Nesingwary (GVG_120).

Card Text: <b>Battlecry:</b> Destroy a Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()