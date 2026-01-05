"""Effect for Illuminate (TSC_210).

Card Text: <b>Dredge</b>. If it's a spell,
reduce its Cost by (3).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass