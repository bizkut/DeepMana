"""Effect for Timeless Causality (TIME_061).

Card Text: <b>Battlecry:</b> Reverse the order of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass