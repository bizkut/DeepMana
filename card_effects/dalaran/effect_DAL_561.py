"""Effect for Jumbo Imp (DAL_561).

Card Text: Costs (1) less whenever a friendly Demon dies while this is in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass