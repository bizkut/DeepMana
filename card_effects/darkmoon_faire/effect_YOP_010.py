"""Effect for Imprisoned Celestial (YOP_010).

Card Text: [x]<b>Dormant</b> for 2 turns.
<b>Spellburst</b>: Give your minions
<b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2