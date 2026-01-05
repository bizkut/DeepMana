"""Effect for Aeon Reaver (YOD_014).

Card Text: <b>Battlecry:</b> Deal damage to a minion equal to its Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)