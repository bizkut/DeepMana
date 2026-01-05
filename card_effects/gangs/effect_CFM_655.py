"""Effect for Toxic Sewer Ooze (CFM_655).

Card Text: <b>Battlecry:</b> Remove 1 Durability from your opponent's weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass