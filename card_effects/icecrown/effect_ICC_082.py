"""Effect for Frozen Clone (ICC_082).

Card Text: <b>Secret:</b> After your opponent plays a minion, add two copies of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass