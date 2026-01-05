"""Effect for SI:7 Agent (EX1_134).

Card Text: <b>Combo:</b> Deal 3 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)