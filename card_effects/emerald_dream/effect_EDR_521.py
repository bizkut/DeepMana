"""Effect for Tricky Satyr (EDR_521).

Card Text: <b>Battlecry:</b> Get a copy of the lowest Cost card in your opponent's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass