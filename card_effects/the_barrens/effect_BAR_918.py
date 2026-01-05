"""Effect for Tamsin Roame (BAR_918).

Card Text: [x]Whenever you cast a Shadow
spell that costs (1) or more,
add a copy to your hand
that costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass