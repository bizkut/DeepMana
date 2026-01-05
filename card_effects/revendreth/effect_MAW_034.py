"""Effect for The Jailer (MAW_034).

Card Text: <b>Battlecry:</b> Destroy your deck. This minion
gains <b>Immune</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()