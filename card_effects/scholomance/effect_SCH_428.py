"""Effect for Lorekeeper Polkelt (SCH_428).

Card Text: [x]<b>Battlecry:</b> Reorder your deck
from the highest Cost card
to the lowest Cost card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass