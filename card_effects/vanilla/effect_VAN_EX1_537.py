"""Effect for Explosive Shot (VAN_EX1_537).

Card Text: Deal $5 damage to a minion and $2 damage to adjacent ones.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)