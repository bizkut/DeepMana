"""Effect for Granite Forgeborn (SW_032).

Card Text: <b>Battlecry:</b> Reduce the Cost of Elementals in your hand and deck by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass