"""Effect for Anonymous Informant (REV_841).

Card Text: <b>Battlecry:</b> The next <b>Secret</b> you play costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass