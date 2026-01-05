"""Effect for Shimmering Courser (LOOT_193).

Card Text: <b>Elusive</b> on your 
opponent's turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass