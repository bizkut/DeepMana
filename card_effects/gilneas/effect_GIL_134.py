"""Effect for Holy Water (GIL_134).

Card Text: Deal $4 damage to a minion. If that kills it, add a copy of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)