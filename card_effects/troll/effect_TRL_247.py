"""Effect for Soulwarden (TRL_247).

Card Text: <b>Battlecry:</b> Add 3 random cards you discarded this game to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass