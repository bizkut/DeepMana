"""Effect for Mana Wraith (EX1_616).

Card Text: ALL minions cost (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass