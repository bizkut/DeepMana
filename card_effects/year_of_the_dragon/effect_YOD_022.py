"""Effect for Risky Skipper (YOD_022).

Card Text: After you play a minion, deal 1 damage to all minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)