"""Effect for Demolition Renovator (REV_023).

Card Text: <b>Tradeable</b>
<b>Battlecry:</b> Destroy 
an enemy location.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()