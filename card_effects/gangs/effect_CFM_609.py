"""Effect for Fel Orc Soulfiend (CFM_609).

Card Text: At the start of your turn, deal 2 damage to this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)