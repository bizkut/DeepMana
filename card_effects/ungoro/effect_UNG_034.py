"""Effect for Radiant Elemental (UNG_034).

Card Text: Your spells cost (1) less
<i>(but not less than 1)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass