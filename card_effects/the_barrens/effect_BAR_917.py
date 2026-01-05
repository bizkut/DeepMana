"""Effect for Barrens Scavenger (BAR_917).

Card Text: [x]<b>Taunt</b>
Costs (1) while your deck
has 10 or fewer cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass