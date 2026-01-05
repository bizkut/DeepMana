"""Effect for Darkbishop Benedictus (CORE_SW_448).

Card Text: <b>Start of Game:</b> If the spells in your deck are all Shadow, enter Shadowform.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass