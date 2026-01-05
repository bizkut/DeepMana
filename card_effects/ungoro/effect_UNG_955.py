"""Effect for Meteor (UNG_955).

Card Text: Deal $15 damage to a minion and $4 damage to adjacent ones.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 15, source)