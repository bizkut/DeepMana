"""Effect for Wandmaker (CORE_SCH_160).

Card Text: <b>Battlecry:</b> Add a 1-Cost spell from your class to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass