"""Effect for Captain Galvangar (AV_145).

Card Text: [x]<b>Battlecry:</b> If you have
gained 15 or more Armor
this game, gain +3/+3
and <b>Charge</b>.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 15
        target._max_health += 15