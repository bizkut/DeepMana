"""Effect for Wyrmrest Purifier (DRG_062).

Card Text: [x]<b>Battlecry:</b> Transform all
Neutral cards in your deck
into random cards from
your class.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass