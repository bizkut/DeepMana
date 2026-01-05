"""Effect for Yogg-Saron, Master of Fate (DMF_004).

Card Text: [x]<b>Battlecry:</b> If you've cast
10 spells this game, spin
the Wheel of Yogg-Saron.@
<i>({0} left!)</i>@
<i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass