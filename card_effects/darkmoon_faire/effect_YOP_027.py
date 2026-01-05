"""Effect for Bola Shot (YOP_027).

Card Text: Deal $1 damage to a minion and $2 damage to its neighbors.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)