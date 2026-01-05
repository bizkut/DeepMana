"""Effect for Cabal Shadow Priest (EX1_091).

Card Text: <b>Battlecry:</b> Take control of an enemy minion that has 2 or less Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass