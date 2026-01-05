"""Effect for Hopeful Dryad (EDR_001).

Card Text: <b>Battlecry:</b> Get a random Dream card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass