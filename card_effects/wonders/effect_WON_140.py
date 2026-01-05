"""Effect for Future Emissary (WON_140).

Card Text: [x]<b>Battlecry:</b> Reduce the Cost
of all Dragons in your hand
 by (1). Give them +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1