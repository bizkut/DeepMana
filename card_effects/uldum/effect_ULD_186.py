"""Effect for Pharaoh Cat (ULD_186).

Card Text: <b>Battlecry:</b> Add a random <b>Reborn</b> minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass