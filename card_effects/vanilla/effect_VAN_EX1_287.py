"""Effect for Counterspell (VAN_EX1_287).

Card Text: <b>Secret:</b> When your opponent casts a spell, <b>Counter</b> it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass