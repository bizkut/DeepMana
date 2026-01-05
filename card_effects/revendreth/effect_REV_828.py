"""Effect for Kidnap (REV_828).

Card Text: <b>Secret:</b> After your opponent plays a minion, stuff it in a 0/4 Sack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass