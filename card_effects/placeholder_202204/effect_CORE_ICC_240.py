"""Effect for Runeforge Haunter (CORE_ICC_240).

Card Text: During your turn, your weapon doesn't lose Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass