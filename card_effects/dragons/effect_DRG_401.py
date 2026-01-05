"""Effect for Grizzled Wizard (DRG_401).

Card Text: <b>Battlecry:</b> Swap Hero Powers with your opponent until your next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass