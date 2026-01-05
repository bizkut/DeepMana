"""Effect for Keeper Stalladris (DAL_732).

Card Text: After you cast a <b>Choose One</b> spell, add copies of both choices to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass