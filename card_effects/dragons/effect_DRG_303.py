"""Effect for Disciple of Galakrond (DRG_303).

Card Text: <b>Battlecry:</b> <b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass