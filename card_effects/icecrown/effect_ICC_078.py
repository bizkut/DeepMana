"""Effect for Avalanche (ICC_078).

Card Text: <b>Freeze</b> a minion and deal $3 damage to adjacent ones.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)