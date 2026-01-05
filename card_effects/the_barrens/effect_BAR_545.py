"""Effect for Arcane Luminary (BAR_545).

Card Text: [x]Cards that didn't start in
your deck cost (2) less
<i>(but not less than 1)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass