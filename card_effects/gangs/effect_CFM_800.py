"""Effect for Getaway Kodo (CFM_800).

Card Text: <b>Secret:</b> When a friendly minion dies, return it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass