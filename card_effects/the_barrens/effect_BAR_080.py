"""Effect for Shadow Hunter Vol'jin (BAR_080).

Card Text: <b>Battlecry:</b> Choose a minion. Swap it with a random one in its owner's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass