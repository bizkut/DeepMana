"""Effect for Hex (VAN_EX1_246).

Card Text: Transform a minion into a 0/1 Frog with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass