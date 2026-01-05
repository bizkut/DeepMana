"""Effect for Corporal (AV_122).

Card Text: <b>Honorable Kill:</b> Give
your other minions
<b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1