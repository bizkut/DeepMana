"""Effect for Lunar Eclipse (DMF_057).

Card Text: Deal $3 damage to a minion. Your next spell this turn costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)