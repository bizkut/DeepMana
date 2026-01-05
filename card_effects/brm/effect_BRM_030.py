"""Effect for Nefarian (BRM_030).

Card Text: <b>Battlecry:</b> Add 2 random spells to your hand <i>(from your opponent's class)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass