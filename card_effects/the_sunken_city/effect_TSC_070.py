"""Effect for Harpoon Gun (TSC_070).

Card Text: After your hero attacks, <b>Dredge</b>. If it's a Beast, reduce its Cost by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass