"""Effect for Depth Charge (DRG_078).

Card Text: At the start of your turn, deal 5 damage to ALL minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)