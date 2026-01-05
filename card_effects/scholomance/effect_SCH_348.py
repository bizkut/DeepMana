"""Effect for Combustion (SCH_348).

Card Text: [x]Deal $4 damage to
a minion. Any excess
damages both neighbors.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)