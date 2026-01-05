"""Effect for Animated Armor (LOE_119).

Card Text: Your hero can only take 1 damage at a time.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass