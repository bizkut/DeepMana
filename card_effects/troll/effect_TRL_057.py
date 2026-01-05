"""Effect for Serpent Ward (TRL_057).

Card Text: At the end of your turn,
deal 2 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)