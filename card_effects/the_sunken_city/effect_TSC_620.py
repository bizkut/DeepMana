"""Effect for Spitelash Siren (TSC_620).

Card Text: [x]After you play a Naga,
refresh two Mana Crystals.
<i>(Then switch to spell!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass