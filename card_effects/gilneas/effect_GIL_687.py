"""Effect for WANTED! (GIL_687).

Card Text: Deal $3 damage to a minion. If that kills it, add a Coin to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)