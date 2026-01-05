"""Effect for Dreadlord's Bite (DMF_227).

Card Text: [x]<b>Outcast:</b> Deal 1 damage
to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)