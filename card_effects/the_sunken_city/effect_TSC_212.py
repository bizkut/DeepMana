"""Effect for Handmaiden (TSC_212).

Card Text: [x]<b>Battlecry:</b> If you've cast
three spells while holding
this, draw 3 cards.@
<i>({0} left!)</i>@
<i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)