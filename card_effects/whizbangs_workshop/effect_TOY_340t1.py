"""Effect for Nostalgic Initiate (TOY_340t1).

Card Text: <b>Mini</b> The first time you cast a spell, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
