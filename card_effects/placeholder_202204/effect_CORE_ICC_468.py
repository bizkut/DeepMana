"""Effect for Wretched Tiller (CORE_ICC_468).

Card Text: Whenever this minion attacks, deal 2 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)