"""Effect for Cheaty Snobold (AV_251).

Card Text: After an enemy is <b>Frozen</b>, deal 3 damage to it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)