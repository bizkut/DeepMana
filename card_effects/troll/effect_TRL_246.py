"""Effect for Void Contract (TRL_246).

Card Text: Destroy half of each player's deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()