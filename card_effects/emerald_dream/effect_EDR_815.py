"""Effect for Corpse Flower (EDR_815).

Card Text: After your opponent summons a minion,
spend 2 <b>Corpses</b> to deal 3 damage to it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)