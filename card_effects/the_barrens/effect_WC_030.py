"""Effect for Mutanus the Devourer (WC_030).

Card Text: [x]<b>Battlecry:</b> Eat a minion in
your opponent's hand.
Gain its stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass