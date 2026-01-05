"""Effect for Thrall, Deathseer (ICC_481).

Card Text: <b>Battlecry:</b> Transform your minions into random ones that cost (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass