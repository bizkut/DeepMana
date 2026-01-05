"""Effect for Coliseum Manager (AT_110).

Card Text: <b>Inspire:</b> Return this minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass