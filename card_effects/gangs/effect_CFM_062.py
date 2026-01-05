"""Effect for Grimestreet Protector (CFM_062).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Give adjacent
 minions <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1