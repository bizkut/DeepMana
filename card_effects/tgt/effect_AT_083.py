"""Effect for Dragonhawk Rider (AT_083).

Card Text: <b>Inspire:</b> Gain <b>Windfury</b>
this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass