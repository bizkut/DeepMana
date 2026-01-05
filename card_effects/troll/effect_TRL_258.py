"""Effect for Mass Hysteria (TRL_258).

Card Text: Force each minion to attack another random minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass