"""Effect for Starsurge (EDR_941).

Card Text: Deal $1 damage to a minion. <i>(Improved by each friendly minion that died this game.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)