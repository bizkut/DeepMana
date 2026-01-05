"""Effect for Runeforge Haunter (ICC_240).

Card Text: During your turn, your weapon doesn't lose Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass