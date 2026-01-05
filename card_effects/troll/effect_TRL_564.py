"""Effect for Mojomaster Zihi (TRL_564).

Card Text: <b>Battlecry:</b> Set each player to 5 Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass