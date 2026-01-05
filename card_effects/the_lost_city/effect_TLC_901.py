"""Effect for Fumigate (TLC_901).

Card Text: Deal $3 damage to a minion and all others of the same minion type.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)