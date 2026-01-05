"""Effect for Totem Cruncher (GIL_583).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Destroy your Totems. Gain +2/+2 for each destroyed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()