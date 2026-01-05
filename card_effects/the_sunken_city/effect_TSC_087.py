"""Effect for Commander Sivara (TSC_087).

Card Text: [x]<b>Battlecry:</b> If you've cast
three spells while holding
this, add those spells back
to your hand.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass