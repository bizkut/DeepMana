"""Effect for Baleful Banker (GIL_815).

Card Text: <b>Battlecry:</b> Choose a friendly minion. Shuffle a copy into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass