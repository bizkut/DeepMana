"""Effect for SI:7 Agent (VAN_EX1_134).

Card Text: <b>Combo:</b> Deal 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)