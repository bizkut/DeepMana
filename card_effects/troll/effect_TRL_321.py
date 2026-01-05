"""Effect for Devastate (TRL_321).

Card Text: Deal $4 damage to a damaged minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)