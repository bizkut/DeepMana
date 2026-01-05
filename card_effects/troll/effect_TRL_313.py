"""Effect for Scorch (TRL_313).

Card Text: [x]Deal $4 damage to a
minion. Costs (1) if you
played an Elemental
last turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)