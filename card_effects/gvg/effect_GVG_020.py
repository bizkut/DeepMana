"""Effect for Fel Cannon (GVG_020).

Card Text: At the end of your turn, deal 2 damage to a non-Mech minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)