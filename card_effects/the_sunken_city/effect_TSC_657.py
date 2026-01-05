"""Effect for Dozing Kelpkeeper (TSC_657).

Card Text: [x]<b>Rush</b>. Starts <b>Dormant</b>.
After you've cast 5 Mana
 worth of spells, awaken.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass