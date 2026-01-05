"""Effect for Violet Illusionist (KAR_712).

Card Text: During your turn, your hero is <b>Immune</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass