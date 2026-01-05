"""Effect for Hydralodon (TSC_950).

Card Text: [x]<b>Colossal +2</b>
<b>Battlecry:</b> Give your
 Hydralodon Heads <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2