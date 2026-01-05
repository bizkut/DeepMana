"""Effect for Contract Conjurer (MAW_101).

Card Text: Costs (3) less for each <b>Secret</b> you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass