"""Effect for Grievous Bite (UNG_910).

Card Text: Deal $3 damage to a minion and $1 damage to adjacent ones.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)