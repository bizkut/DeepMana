"""Effect for Sea Reaver (AT_130).

Card Text: When you draw this, deal 1 damage to your minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)