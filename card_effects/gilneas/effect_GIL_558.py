"""Effect for Swamp Leech (GIL_558).

Card Text: <b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass