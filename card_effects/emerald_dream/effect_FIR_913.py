"""Effect for Inferno Herald (FIR_913).

Card Text: [x]After you cast a Fire spell,
get a random Elemental and
reduce its Cost by (3).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass