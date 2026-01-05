"""Effect for Animated Berserker (CORE_ICC_238).

Card Text: After you play a minion, deal 1 damage to it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)