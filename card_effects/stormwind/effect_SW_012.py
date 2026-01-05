"""Effect for Shadowcloth Needle (SW_012).

Card Text: [x]After you cast a Shadow
spell, deal 1 damage
to all enemies.
Lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)