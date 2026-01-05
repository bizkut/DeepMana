"""Effect for Ancient Krakenbane (TID_074).

Card Text: [x]<b>Battlecry:</b> If you've cast
three spells while holding
this, deal 5 damage.@
<i>({0} left!)</i>@
<i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)