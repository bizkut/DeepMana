"""Effect for Bandersmosh (DRG_096).

Card Text: [x]Each turn this is in your
hand, transform it into a
5/5 copy of a random
<b>Legendary</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass