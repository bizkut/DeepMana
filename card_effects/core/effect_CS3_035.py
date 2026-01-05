"""Effect for Nozdormu the Eternal (CS3_035).

Card Text: [x]<b>Start of Game:</b> If this is in BOTH players' decks, turns  are only 15 seconds long.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
