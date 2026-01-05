"""Effect for Libram of Judgment (YOP_011).

Card Text: <b>Corrupt:</b> Gain <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass