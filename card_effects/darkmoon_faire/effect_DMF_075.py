"""Effect for Guess the Weight (DMF_075).

Card Text: Draw a card. Guess if your next card costs more or less to draw it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)