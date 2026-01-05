"""Effect for Ancient Brewmaster (EX1_057).

Card Text: <b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass