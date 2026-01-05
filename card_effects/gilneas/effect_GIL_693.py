"""Effect for Blood Witch (GIL_693).

Card Text: At the start of your turn, deal 1 damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)