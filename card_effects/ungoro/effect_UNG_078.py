"""Effect for Tortollan Forager (UNG_078).

Card Text: <b>Battlecry:</b> Add a random minion with 5 or more Attack to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass