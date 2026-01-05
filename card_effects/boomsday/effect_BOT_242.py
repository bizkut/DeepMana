"""Effect for Myra's Unstable Element (BOT_242).

Card Text: Draw the rest of
your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)