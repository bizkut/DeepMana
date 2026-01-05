"""Effect for Brave Archer (AT_059).

Card Text: <b>Inspire:</b> If your hand is empty, deal 2 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)