"""Effect for Pufferfist (TSC_002).

Card Text: After your hero attacks, deal 1 damage to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)