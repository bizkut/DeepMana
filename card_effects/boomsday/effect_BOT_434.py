"""Effect for Flobbidinous Floop (BOT_434).

Card Text: While in your hand, this is a 3/4 copy of the last minion you played.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass