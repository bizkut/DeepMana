"""Effect for Undercity Valiant (AT_030).

Card Text: <b>Combo:</b> Deal 1 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)