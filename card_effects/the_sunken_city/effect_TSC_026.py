"""Effect for Colaque (TSC_026).

Card Text: [x]<b>Colossal +1</b>
 <b>Immune</b> while you control
Colaque's Shell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1