"""Effect for Mad Summoner (DAL_751).

Card Text: [x]<b>Battlecry:</b> Fill each player's
board with 1/1 Imps.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass