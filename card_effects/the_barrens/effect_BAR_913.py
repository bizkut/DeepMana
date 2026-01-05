"""Effect for Altar of Fire (BAR_913).

Card Text: Destroy the top 3 cards of each deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()