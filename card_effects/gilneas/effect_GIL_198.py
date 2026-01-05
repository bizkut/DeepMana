"""Effect for Azalina Soulthief (GIL_198).

Card Text: <b>Battlecry:</b> Replace your hand with a copy of your opponent's.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass