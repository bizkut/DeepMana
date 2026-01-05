"""Effect for The Harvester of Envy (CORE_REV_011).

Card Text: After you play a card copied from the opponent, steal the original.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass