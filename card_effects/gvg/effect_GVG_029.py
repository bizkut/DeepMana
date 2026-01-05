"""Effect for Ancestor's Call (GVG_029).

Card Text: Put a random minion from each player's hand into the battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass