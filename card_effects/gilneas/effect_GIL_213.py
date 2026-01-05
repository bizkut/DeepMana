"""Effect for Tanglefur Mystic (GIL_213).

Card Text: <b>Battlecry:</b> Add a random
2-Cost minion to each player's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass