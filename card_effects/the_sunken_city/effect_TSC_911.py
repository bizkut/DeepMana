"""Effect for Excavation Specialist (TSC_911).

Card Text: <b>Battlecry:</b> <b>Dredge</b>.
Reduce its Cost by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass