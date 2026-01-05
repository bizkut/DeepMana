"""Effect for King Mukla (CORE_EX1_014).

Card Text: <b>Battlecry:</b> Give your opponent 2 Bananas.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
