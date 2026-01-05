"""Effect for Mysterious Visitor (REV_246).

Card Text: <b>Battlecry:</b> Reduce the Cost of cards copied from your opponent by (3).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass