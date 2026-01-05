"""Effect for Moonbeam (TID_001).

Card Text: Deal $1 damage to an enemy, twice.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)