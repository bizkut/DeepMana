"""Effect for Contingency (TIME_023).

Card Text: Draw the bottom two cards from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)