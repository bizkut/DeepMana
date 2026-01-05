"""Effect for Dark Pharaoh Tekahn (ULD_168).

Card Text: <b>Battlecry:</b> For the rest of the game, your <b>Lackeys</b> are 4/4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass