"""Effect for Earth Shock (EX1_245).

Card Text: <b>Silence</b> a minion, then deal $1 damage to it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)