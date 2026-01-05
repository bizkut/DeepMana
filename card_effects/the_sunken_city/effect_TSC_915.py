"""Effect for Bone Glaive (TSC_915).

Card Text: <b>Battlecry:</b> <b>Dredge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass