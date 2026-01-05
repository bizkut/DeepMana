"""Effect for Flame Lance (AT_001).

Card Text: Deal $25 damage
to a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 25, source)