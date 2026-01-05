"""Effect for Enchanter (RLK_952).

Card Text: Enemy minions take double damage during your turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass