"""Effect for Mo'arg Artificer (BT_733).

Card Text: All minions take double damage from spells.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass