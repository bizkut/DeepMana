"""Effect for Dragon Consort (BRM_018).

Card Text: <b>Battlecry:</b> The next Dragon you play costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass