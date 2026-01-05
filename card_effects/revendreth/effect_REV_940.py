"""Effect for Necrolord Draka (REV_940).

Card Text: [x]<b>Battlecry:</b> Equip a 1/3
Dagger. <i>(+1 Attack for
each other card you played
this turn, up to 10!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1