"""Effect for Corrupt Elementalist (DRG_218).

Card Text: <b>Battlecry:</b> <b>Invoke</b> Galakrond twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass