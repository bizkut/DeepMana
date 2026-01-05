"""Effect for Frizz Kindleroost (DRG_257).

Card Text: <b>Battlecry:</b> Reduce the Cost of Dragons in your deck by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass