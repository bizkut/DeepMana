"""Effect for Tight-Lipped Witness (MAW_032).

Card Text: <b>Secrets</b> can't be revealed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass