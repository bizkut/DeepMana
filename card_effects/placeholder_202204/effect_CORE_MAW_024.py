"""Effect for Dew Process (CORE_MAW_024).

Card Text: [x]For the rest of the game,
players draw an extra card
at the start of their turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)