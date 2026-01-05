"""Effect for Quantum Destabilizer (TIME_060).

Card Text: This minion takes double damage from all sources.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass