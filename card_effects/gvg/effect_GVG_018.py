"""Effect for Queen of Pain (GVG_018).

Card Text: <b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass