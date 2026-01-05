"""Effect for Stormwind Champion (CORE_CS2_222).

Card Text: Your other minions have +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
