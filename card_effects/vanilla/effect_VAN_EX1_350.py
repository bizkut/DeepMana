"""Effect for Prophet Velen (VAN_EX1_350).

Card Text: Double the damage and healing of your spells and Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)