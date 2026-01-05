"""Effect for Polymorph: Boar (AT_005).

Card Text: Transform a minion into a 4/2 Boar with <b>Charge</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass