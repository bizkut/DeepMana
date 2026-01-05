"""Effect for Cone of Cold (VAN_EX1_275).

Card Text: <b>Freeze</b> a minion and the minions next to it, and deal $1 damage to them.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)